#!/usr/bin/env python3
"""Search reviewed Mobbin references without third-party dependencies."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('query', nargs='?', default='')
parser.add_argument('--tag', help='Exact pattern tag')
parser.add_argument('--kind', choices=['screen', 'section', 'flow'])
parser.add_argument('--json', action='store_true')
parser.add_argument('--include-needs-review', action='store_true', help='Include visually inconclusive references')
args = parser.parse_args()
records = json.loads((ROOT/'skills/mobbin-site-builder/references/library.json').read_text())
hits = []
for r in records:
    if not args.include_needs_review and not r.get('usable', True):
        continue
    searchable = json.dumps({k:r[k] for k in ('site','title','tags','observations')}, ensure_ascii=False).casefold()
    if args.query.casefold() not in searchable:
        continue
    if args.tag and args.tag not in r['tags']:
        continue
    if args.kind and args.kind != r['kind']:
        continue
    hits.append(r)
if args.json:
    print(json.dumps(hits, ensure_ascii=False, indent=2))
else:
    for r in hits:
        print(f'{r["site"]}\t{r["kind"]}\t{r["title"]}\t{", ".join(r["tags"])}\n  {r["mobbin_url"]}')
    print(f'결과: {len(hits)}개')
