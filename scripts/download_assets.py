#!/usr/bin/env python3
"""Download original images from a private Mobbin manifest; never preview bytes."""
import argparse
import concurrent.futures
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('manifest', type=Path)
args = parser.parse_args()
records = json.loads(args.manifest.read_text())
destination = ROOT / 'assets/library'
destination.mkdir(parents=True, exist_ok=True)


def download(r):
    screen_id = r['id']
    if any(c not in '0123456789abcdef-' for c in screen_id):
        raise ValueError(f'Invalid image identifier: {screen_id}')
    path = destination / f'{screen_id}.jpg'
    if path.exists() and path.stat().st_size > 0:
        return True, screen_id, 'existing'
    try:
        with urllib.request.urlopen(r['image_url'], timeout=45) as response:
            body = response.read()
        if not body.startswith(b'\xff\xd8'):
            raise ValueError('Expected JPEG original')
        temporary = path.with_suffix('.part')
        temporary.write_bytes(body)
        temporary.replace(path)
        return True, screen_id, 'downloaded'
    except Exception as exc:
        # Do not expose expiring URLs in logs.
        return False, screen_id, type(exc).__name__


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results = list(pool.map(download, records))
report = dict(total=len(results), downloaded=sum(x[0] for x in results),
              failures=[dict(id=x[1], error=x[2]) for x in results if not x[0]])
(ROOT/'assets/download-report.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
raise SystemExit(1 if report['failures'] else 0)
