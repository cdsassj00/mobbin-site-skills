#!/usr/bin/env python3
"""Install one portable skill into supported coding agents; no network needed."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skills/mobbin-site-builder'
NAME = 'mobbin-site-builder'
MARKER = '.mobbin-site-skills-install.json'
AGENTS = ('claude', 'codex', 'opencode', 'grok')


def target(agent, project=None):
    if project is not None:
        paths = {'claude':'.claude/skills', 'codex':'.agents/skills',
                 'opencode':'.opencode/skills', 'grok':'.grok/skills'}
        return Path(project).resolve() / paths[agent] / NAME
    home = Path.home()
    return {'claude':home/'.claude/skills', 'codex':home/'.agents/skills',
            'opencode':Path(os.environ.get('XDG_CONFIG_HOME', home/'.config'))/'opencode/skills',
            'grok':home/'.grok/skills'}[agent] / NAME


def preflight(dest, replace):
    if dest.is_symlink():
        raise ValueError(f'기존 심볼릭 링크를 변경하지 않습니다: {dest}')
    if dest.exists():
        if not replace:
            raise ValueError(f'이미 설치됨: {dest}. 이 설치기로 설치한 스킬은 --replace로 갱신하세요.')
        marker = dest / MARKER
        if not marker.is_file() or json.loads(marker.read_text()).get('package') != 'mobbin-site-skills':
            raise ValueError(f'다른 설치 내용을 덮어쓰지 않습니다: {dest}')


def install(dest, replace=False, text_only=False):
    preflight(dest, replace)
    dest.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.mobbin-install-', dir=dest.parent))
    backup = None
    try:
        ignored = shutil.ignore_patterns('*.jpg','*.png','*.webp') if text_only else None
        shutil.copytree(SOURCE, staging/'skill', ignore=ignored)
        (staging/'skill'/MARKER).write_text(json.dumps(dict(package='mobbin-site-skills',version='2.0.0',images=not text_only))+'\n')
        if dest.exists():
            stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup = dest.with_name(dest.name+'.backup-'+stamp)
            dest.rename(backup)
        try:
            (staging/'skill').rename(dest)
        except Exception:
            if backup:
                backup.rename(dest)
            raise
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return dict(destination=str(dest), backup=str(backup) if backup else None, images=not text_only)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=(*AGENTS, 'all'), required=True)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--project', type=Path, help='Target project root')
    scope.add_argument('--global', dest='global_scope', action='store_true')
    parser.add_argument('--replace', action='store_true', help='Update own installs with a backup')
    parser.add_argument('--text-only', action='store_true', help='Skip images to reduce size; textual guidance remains offline')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    selected = AGENTS if args.agent=='all' else [args.agent]
    targets = [target(a,args.project) for a in selected]
    # Check every destination before changing any.
    for dest in targets:
        preflight(dest,args.replace)
    if args.dry_run:
        print(json.dumps([str(p) for p in targets],ensure_ascii=False,indent=2))
        return
    for dest in targets:
        print(json.dumps(install(dest,args.replace,args.text_only),ensure_ascii=False))


if __name__=='__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(2)
