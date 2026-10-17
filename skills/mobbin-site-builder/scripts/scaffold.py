#!/usr/bin/env python3
"""Generate a dependency-free, functional UI starting point offline."""
import argparse
import html
import json
from pathlib import Path
import shutil
import sys
from design_engine import SKILL, read, load_brief, recommend, css_tokens

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--brief', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--style', help='Override recommended style ID')
parser.add_argument('--layout', help='Override inferred layout ID')
args = parser.parse_args()
try:
    brief = load_brief(args.brief)
    result = recommend(brief)
    if result['missing']:
        raise ValueError('먼저 브리프 질문에 답하세요: '+', '.join(result['missing']))
    if not result['directions']:
        raise ValueError('모든 스타일이 제외됐습니다. constraints.avoid를 조정하세요.')
    style_id = args.style or result['directions'][0]['style']['id']
    style = next((s for s in read('styles.json') if s['id']==style_id), None)
    layout_id = args.layout or result['layout']['id']
    layout = next((x for x in read('layouts.json') if x['id']==layout_id), None)
    if not style or not layout:
        raise ValueError('Unknown style or layout')
    tokens = css_tokens(style, brief.get('brand', {}).get('accent') or None)
    out = Path(args.output).resolve()
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError('출력 경로가 비어 있지 않습니다. 새 폴더를 지정하세요.')
    title = brief.get('brand', {}).get('name') or '새로운 서비스'
    if not isinstance(title, str):
        raise ValueError('brand.name must be a string')
    source = SKILL / 'assets/starter'
    document = (source/'index.html').read_text().replace('__TITLE__', html.escape(title)).replace('__STYLE__', html.escape(style_id)).replace('__LAYOUT__', html.escape(layout_id))
    out.mkdir(parents=True, exist_ok=True)
    (out/'index.html').write_text(document)
    (out/'style.css').write_text(tokens+(source/'base.css').read_text())
    shutil.copyfile(source/'app.js', out/'app.js')
    config = dict(brief=brief,style=style,layout=layout)
    (out/'config.js').write_text('window.DESIGN_CONFIG = '+json.dumps(config,ensure_ascii=False).replace('<','\\u003c')+';\n')
    (out/'design-spec.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
    (out/'README.md').write_text(f'# {title}\n\n이 예제는 로컬 데모입니다. 실제 결제·예약·계정 생성·메시지 발송을 하지 않습니다.\n\n실행: `python -m http.server 8000 --directory "{out}"`\n\n선택 스타일: {style_id}\n구조: {layout_id}\n출시 전 실제 데이터·브랜드 에셋·API를 연결하세요.\n')
    print(json.dumps(dict(output=str(out),style=style_id,layout=layout_id,offline=True),ensure_ascii=False))
except (ValueError, OSError) as exc:
    print(str(exc), file=sys.stderr)
    raise SystemExit(2)
