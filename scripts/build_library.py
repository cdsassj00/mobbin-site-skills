#!/usr/bin/env python3
"""Build portable, searchable skill references from reviewed Mobbin records."""
import argparse
import collections
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/mobbin-site-builder'
DATA = SKILL / 'references/library.json'


def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-') or 'site'


def validate(records):
    ids = set()
    for r in records:
        for key in ('id', 'site', 'kind', 'mobbin_url', 'tags', 'observations'):
            if key not in r:
                raise ValueError(f'Missing {key}: {r.get("id")}')
        if r['id'] in ids:
            raise ValueError(f'Duplicate reference: {r["id"]}')
        ids.add(r['id'])
        if r['kind'] not in ('screen', 'section', 'flow'):
            raise ValueError(f'Unknown kind: {r["kind"]}')
        if not r['mobbin_url'].startswith('https://mobbin.com/'):
            raise ValueError(f'Invalid source: {r["id"]}')
        if not r['observations'] or not r['tags']:
            raise ValueError(f'Unreviewed reference: {r["id"]}')
        if 'image_url' in r:
            raise ValueError('Expiring image URLs belong in private assets manifests')
        for o in r['observations']:
            if not o.get('note') or not o.get('screen_id'):
                raise ValueError(f'Invalid observation: {r["id"]}')
        if r['kind'] == 'flow':
            screens = r.get('screens', [])
            if len(screens) != r.get('screen_count'):
                raise ValueError(f'Incomplete flow metadata: {r["id"]}')
            known = {s['id'] for s in screens}
            if any(o['screen_id'] not in known for o in r['observations']):
                raise ValueError(f'Unknown observed flow screen: {r["id"]}')


def build():
    records = json.loads(DATA.read_text())
    validate(records)
    groups = collections.defaultdict(list)
    for r in records:
        groups[r['site']].append(r)
    docs = SKILL / 'references/library/sites'
    docs.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, items in sorted(groups.items(), key=lambda x: x[0].casefold()):
        filename = f'{slug(name)}-{items[0]["id"][:8]}.md'
        paths[name] = f'library/sites/{filename}'
        text = [f'# {name}', '', '이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.', '']
        for r in items:
            text += [f'## {r["title"]}', '', f'- 자료 유형: {r["kind"]}',
                     f'- 출처: [{name} — Mobbin]({r["mobbin_url"]})',
                     f'- 확인 날짜: {r.get("reviewed_at", "2026-10-11")}',
                     '- 패턴: ' + ', '.join(r['tags']), '', '### 직접 관찰', '']
            for o in r['observations']:
                prefix = f'단계 {o["position"]}: ' if o.get('position') else ''
                text += ['- ' + prefix + o['note']]
                if o.get('local_asset'):
                    text += ['', f'![{name} — 참고 화면](../../../{o["local_asset"]})', '']
            if r['kind'] == 'flow':
                observed = len(r['observations'])
                text += ['', f'전체 {r["screen_count"]}단계 중 직접 확인한 단계는 {observed}개다. 확인하지 않은 단계의 상태·전환은 원본을 보고 확정한다.', '', '### 전체 단계의 클라우드 파일', '']
                text += [f'- {s["position"]}: [로컬 원본](../../../assets/references/{s["id"]}.jpg)' for s in r['screens']]
            else:
                text += ['', f'원본 파일: [오프라인 JPEG](../../../assets/references/{r["id"]}.jpg).']
            text += ['', '### 구현에 적용', '',
                     '- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.',
                     '- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.',
                     '- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.',
                     '- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.', '']
        (docs / filename).write_text('\n'.join(line.rstrip() for line in text))
    by_tag = collections.defaultdict(set)
    for r in records:
        for tag in r['tags']:
            by_tag[tag].add(r['site'])
    counts = collections.Counter(r['kind'] for r in records)
    flow_screens = sum(r.get('screen_count', 0) for r in records)
    observations = sum(len(r['observations']) for r in records)
    stats = dict(sites=len(groups), references=len(records), **counts,
                 flow_screens=flow_screens, observed_images=observations)
    index = ['# Mobbin 레퍼런스 라이브러리', '',
             f'{len(groups)}개 사이트 · {len(records)}개 레퍼런스 (화면 {counts["screen"]}, 섹션 {counts["section"]}, 흐름 {counts["flow"]}).', '',
             f'흐름의 전체 단계 이미지 메타데이터는 {flow_screens}개다. 프리뷰·연락판으로 직접 관찰한 이미지는 총 {observations}개이며, 자료 유형별 확인 범위는 각 명세에 기록한다.', '',
             'Mobbin 전체 목록을 전수 수집한 결과가 아니다. 새 사이트는 MCP로 검색하고 관찰 기록을 추가한다.', '',
             '## 패턴으로 찾기', '']
    for tag, names in sorted(by_tag.items()):
        links = ', '.join(f'[{s}]({paths[s]})' for s in sorted(names))
        index += [f'- **{tag}** ({len(names)}): {links}']
    index += ['', '## 사이트 이름으로 찾기', '', '| 사이트 | 자료 수 | 패턴 |', '| --- | ---: | --- |']
    for name, items in sorted(groups.items(), key=lambda x: x[0].casefold()):
        tags = ', '.join(sorted({t for r in items for t in r['tags']}))
        index += [f'| [{name}]({paths[name]}) | {len(items)} | {tags} |']
    (SKILL / 'references/library-index.md').write_text('\n'.join(index) + '\n')
    (ROOT / 'catalog/README.md').write_text('# 레퍼런스 카탈로그\n\n[전체 사이트와 패턴 인덱스](../skills/mobbin-site-builder/references/library-index.md)\n\n'+json.dumps(stats, ensure_ascii=False, indent=2)+'\n\n초기 7개 명세도 이 폴더에 남아 있다. 확장 자료의 원본 데이터는 스킬 안 `references/library.json`에 있다.\n')
    (SKILL / 'references/library-stats.json').write_text(json.dumps(stats, indent=2)+'\n')
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == '__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    build()
