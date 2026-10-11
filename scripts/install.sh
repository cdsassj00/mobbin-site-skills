#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="${1:-${CODEX_HOME:-$HOME/.codex}/skills}"
destination="$skills_dir/mobbin-site-builder"

if [[ -e "$destination" || -L "$destination" ]]; then
  printf '이미 설치된 경로가 있습니다: %s\n' "$destination" >&2
  exit 1
fi

mkdir -p -- "$skills_dir"
cp -R -- "$repo_root/skills/mobbin-site-builder" "$destination"
printf '설치 완료: %s\n' "$destination"
