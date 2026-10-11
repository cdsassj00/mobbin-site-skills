# Mobbin Site Skills

Mobbin에서 고른 화면과 흐름을 재사용 가능한 구현 명세로 모으는 개인 레퍼런스 저장소.

## 사용하기

1. 에이전트가 연결된 Mobbin MCP로 원하는 화면·섹션·흐름을 검색한다. 기존 `catalog/` 명세도 활용한다.
2. `templates/site-reference.md`를 `catalog/<site-name>.md`로 복사해 관찰한 내용을 기록한다.
3. 아래처럼 에이전트에게 구현을 요청한다.

```text
skills/mobbin-site-builder/SKILL.md를 읽고 적용해줘.
catalog/<site-name>.md와 첨부 스크린샷을 참고해서 사이트를 만들어줘.
브랜드는 내 서비스로 바꾸고, 핵심 화면 흐름과 시각적 밀도를 살려줘.
```

사이트별 기록을 추가하면 같은 스킬로 SaaS, 커머스, 콘텐츠, 예약 등 다양한 사이트를 만들 수 있다. Productboard, Slack, Shop, Etsy, Framer, TravelPerk, Notion의 실제 Mobbin 결과를 수집해 사이트별 명세를 넣었다. `references/site-types.md`는 구현 시작점이며 실제 사이트 분석 결과가 아니다.

## 구조

- `skills/mobbin-site-builder/SKILL.md`: 레퍼런스 분석부터 구현·검증까지의 공통 스킬
- `skills/mobbin-site-builder/references/`: 사이트 유형 및 검증 지침
- `catalog/`: 실제로 확인한 사이트별 명세
- `templates/`: 사이트 및 화면 흐름 기록 양식
- `scripts/install.sh`: 로컬 Codex 스킬 디렉터리에 설치

## Codex에 설치

```bash
bash scripts/install.sh
# 또는 설치 위치 지정
bash scripts/install.sh /path/to/skills
```

기본 설치 위치는 `${CODEX_HOME:-$HOME/.codex}/skills`다. 이미 같은 이름의 스킬이 있으면 덮어쓰지 않는다. 설치 후 새 세션에서 `$mobbin-site-builder`로 호출할 수 있다. 설치하지 않아도 위처럼 파일을 지정해서 사용할 수 있다.

## 레퍼런스 관리

캡처의 출처 URL, 확인 날짜, 데스크톱/모바일 여부를 기록한다. 로그인이나 구독 화면이 도구에서 열리지 않으면 사용자가 제공한 캡처로 작업한다. 원본을 확인하지 못한 내용은 추정으로 표시한다. 원본 이미지 파일은 기본적으로 Git에서 제외하고, 저장소에는 분석 명세를 모은다.
