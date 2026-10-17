#!/usr/bin/env python3
"""Create portable offline release ZIPs and integrity hashes."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/mobbin-site-builder'
DIST=ROOT/'dist'
DIST.mkdir(exist_ok=True)
VERSION='2.0.0'


def archive(path, pairs):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for source,name in sorted(pairs,key=lambda x:x[1]):
            if not source.is_file() or '__pycache__' in source.parts or source.suffix=='.pyc':
                continue
            info=zipfile.ZipInfo(name,date_time=(2026,10,18,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,source.read_bytes())
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None


skillzip=DIST/f'mobbin-site-builder-v{VERSION}.zip'
archive(skillzip,[(p,'mobbin-site-builder/'+p.relative_to(SKILL).as_posix()) for p in SKILL.rglob('*')])
toolkit=DIST/f'mobbin-site-skills-toolkit-v{VERSION}.zip'
files=[]
for directory in ('skills','scripts','docs','tests','templates'):
    files += [(p,'mobbin-site-skills/'+p.relative_to(ROOT).as_posix()) for p in (ROOT/directory).rglob('*')]
for filename in ('README.md','NOTICE.md','VERSION'):
    files.append((ROOT/filename,'mobbin-site-skills/'+filename))
archive(toolkit,files)
checksums=[]
for p in (skillzip,toolkit):
    checksums.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}')
(DIST/'SHA256SUMS.txt').write_text('\n'.join(checksums)+'\n')
print(json.dumps([dict(file=str(p),bytes=p.stat().st_size) for p in (skillzip,toolkit)]))
