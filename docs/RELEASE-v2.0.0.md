# Offline UI Designer & Builder v2.0.0

Mobbin MCP 없이 사용할 수 있는 UI 설계·구현 스킬입니다.

- 목적·대상·핵심 행동과 디자인풍을 질문하고 구조가 다른 UI 방향 3개를 제안합니다.
- 선택한 방향을 명세와 동작하는 코드로 구현합니다.
- Claude Code·Codex·OpenCode·Grok Build용 설치기를 제공합니다.
- 로컬 원본 이미지 350장과 193개 사이트의 295개 레퍼런스, 18개 독자적인 스타일, 8개 동작 예제를 포함합니다.
- 추천·예제 생성에 외부 패키지, Mobbin MCP, 모델 API 키가 필요하지 않습니다.

아래 GitHub 기본 Source code (zip)을 받거나 [저장소 ZIP](https://github.com/cdsassj00/mobbin-site-skills/archive/refs/heads/main.zip)을 다운로드하면 이미지와 설치기까지 포함됩니다. 압축을 풀고 `python scripts/install.py --agent claude --global`을 실행하세요. claude 대신 codex / opencode / grok을 선택할 수 있습니다.

별도 스킬 ZIP과 툴킷 ZIP은 `python scripts/package.py`로 생성합니다. 커스텀 첨부 파일은 GitHub 업로드 서버의 인증 거절로 게시하지 못했습니다. 저장소와 기본 소스 ZIP은 전체 설치 자료를 포함합니다.

전수 수집본은 아닙니다. 전체 카탈로그 내보내기 도구 부재와 요청 제한으로 수집하지 못한 범위를 collection-report.json에 기록했습니다. 원본 이미지·관찰과 독자적인 토큰·예제를 구분합니다.

검증: Python 검사 6개, 8개 핵심 사용자 흐름, 8개 구조의 모바일·데스크톱, 18개 모바일 테마, 외부 요청 0개. 에이전트별 실제 모델 세션 테스트와 로컬 설치·파일 검증은 구분합니다.
