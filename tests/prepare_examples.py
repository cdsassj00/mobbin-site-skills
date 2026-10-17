#!/usr/bin/env python3
"""Generate browser test fixtures from a clean test-output directory."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'.test-output'
SCRIPT=ROOT/'skills/mobbin-site-builder/scripts/scaffold.py'
CASES=[('landing','개발자 API 서비스','가입',['어두운 기술']),
       ('dashboard','업무 관리 대시보드','업무 처리',['밀도 높은']),
       ('commerce','생활용품 쇼핑몰','구매',['선명한']),
       ('editorial','편집형 블로그','읽기',['따뜻한 편집']),
       ('portfolio','디자인 포트폴리오','연락',['흑백']),
       ('booking','여행 숙소 예약','예약',['사진 중심']),
       ('learning','온라인 학습 강의','수강',['학습']),
       ('directory','채용 검색 디렉터리','지원',['기업 신뢰'])]
OUT.mkdir(exist_ok=True)
for layout,purpose,action,vibes in CASES:
    brief=dict(purpose=purpose,audience='일반 사용자',primary_action=action,vibes=vibes,
               pages=[],features=[],brand={'name':'Studio Sample'},constraints={'avoid':[]},assumptions=[])
    source=OUT/f'{layout}.json'
    source.write_text(json.dumps(brief,ensure_ascii=False))
    destination=OUT/layout
    if destination.exists():
        raise SystemExit(f'Test destination exists; preserve it or remove manually: {destination}')
    subprocess.run([sys.executable,str(SCRIPT),'--brief',str(source),'--layout',layout,'--output',str(destination)],check=True)
for style in json.loads((ROOT/'skills/mobbin-site-builder/references/styles.json').read_text()):
    subprocess.run([sys.executable,str(SCRIPT),'--brief',str(OUT/'landing.json'),'--style',style['id'],'--layout','landing','--output',str(OUT/f'theme-{style["id"]}')],check=True)
