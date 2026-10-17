#!/usr/bin/env python3
"""Recommend three UI directions using only bundled design knowledge."""
import argparse
import json
import sys
from design_engine import load_brief, recommend

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--brief', required=True)
parser.add_argument('--output', help='Optional new JSON output file')
args = parser.parse_args()
try:
    result = recommend(load_brief(args.brief))
    output = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.output:
        with open(args.output, 'x', encoding='utf-8') as f:
            f.write(output)
    print(output, end='')
except (ValueError, OSError) as exc:
    print(str(exc), file=sys.stderr)
    raise SystemExit(2)
