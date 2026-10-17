# 코딩 에이전트 호환성

하나의 표준 `SKILL.md`와 같은 상대경로 자료를 사용한다. 모델마다 출력 품질이 같다고 보장하는 의미는 아니다. 설치 경로는 2026-10-18 공식 문서 확인 기준이며, 이 저장소에서는 파일 설치·리소스 완결성과 로컬 추천·예제 실행을 검증한다. 각 제품 계정으로 실제 에이전트 세션을 실행한 결과와는 구분한다.

| 도구 | 프로젝트 설치 위치 | 사용자 전역 위치 | 사용 |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/mobbin-site-builder/` | `~/.claude/skills/mobbin-site-builder/` | `/mobbin-site-builder` 또는 자연어 요청 |
| Codex | `.agents/skills/mobbin-site-builder/` | `~/.agents/skills/mobbin-site-builder/` | `$mobbin-site-builder` 또는 자연어 요청 |
| OpenCode | `.opencode/skills/mobbin-site-builder/` | `~/.config/opencode/skills/mobbin-site-builder/` | skill 도구 또는 자연어 요청 |
| Grok Build | `.grok/skills/mobbin-site-builder/` | `~/.grok/skills/mobbin-site-builder/` | `/mobbin-site-builder`; `grok inspect`로 검색 여부 확인 |

```bash
git clone https://github.com/cdsassj00/mobbin-site-skills.git
cd mobbin-site-skills
python scripts/install.py --agent claude --global
python scripts/install.py --agent codex --project /path/to/project
python scripts/install.py --agent opencode --global
python scripts/install.py --agent grok --global
```

여러 도구를 같은 프로젝트에서 사용하면 `--agent all --project /path/to/project`로 각각 설치할 수 있다. OpenCode는 다른 도구의 호환 디렉터리도 읽으므로 중복 노출되면 사용하는 도구 하나만 설치한다. 기존 설치는 덮어쓰지 않으며, 이 설치기로 만든 스킬만 `--replace`로 백업 후 갱신한다.

## 다른 모델·일반 채팅

모델 이름 자체가 파일 설치 규격을 뜻하지 않는다. Grok을 OpenCode에서 쓰면 OpenCode 설치를 따른다. 일반 Grok/Claude 웹 채팅이나 스킬 로더가 없는 도구에서는 스킬 ZIP을 첨부하거나 저장소 파일을 읽도록 지정한다. 파일·코드 실행 권한이 없는 채팅은 구현 파일을 생성해 안내할 수 있지만 프로젝트를 직접 실행·수정하지는 못한다.

## 검증한 공식 출처

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Codex Skills](https://developers.openai.com/codex/skills/)
- [OpenCode Agent Skills](https://opencode.ai/docs/skills/)
- [Grok Build Skills](https://docs.x.ai/build/features/skills-plugins-marketplaces)

각 도구가 보조 파일을 지연해서 읽는 방식과 도구 권한은 다를 수 있다. 모든 도구에서 적용되도록 스킬 본문에 필수 행동을 두고, Python 명령은 선택 가능한 로컬 도구로 제공한다. MCP는 필수 의존성으로 선언하지 않는다.
