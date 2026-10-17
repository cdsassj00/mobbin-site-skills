---
name: mobbin-site-builder
description: Ask about a website's purpose, audience, visual style, and constraints; propose three UI directions and implement the selected direction using bundled screenshots, site observations, 18 style presets, and offline starters. Use for website design, UI recommendations, frontend implementation, and Mobbin-inspired design. No Mobbin MCP, subscription, API key, or reference-network access required.
---

# Offline UI Designer & Builder

## 기본 원칙

사용자의 사이트 목적과 스타일을 이해한 뒤 구체적인 UI를 제안하고 실제로 구현한다. 기본 모드는 **오프라인**이다. 설치 폴더의 이미지·명세·스타일·스크립트만으로 작업할 수 있다. Mobbin MCP가 없다는 이유로 멈추거나 사용자에게 구독·캡처를 필수로 요구하지 않는다.

이 스킬 폴더를 `<skill>`로 부른다. 상대경로는 현재 프로젝트가 아닌 이 폴더 기준이다. 호스트에 특정 도구나 셸이 있다고 가정하지 않는다. Python이 없으면 마크다운·JSON·예제를 직접 읽어 같은 절차로 작업한다.

## 1. 인터뷰와 프로젝트 확인

[인터뷰 지침](references/intake.md)을 읽는다. 이미 확인한 것은 다시 묻지 말고 빠진 항목만 최대 세 묶음으로 질문한다.

1. **목적·대상·핵심 행동**: 무엇을 위한 사이트이며 누구에게 어떤 행동을 기대하는가?
2. **디자인풍·스타일**: 신뢰감·따뜻함·어두운 기술·선명함·고급스러움 등 어떤 방향을 선호하며 피할 색이나 표현은 무엇인가?
3. **페이지·기능·환경**: 필요한 화면과 동작, 브랜드 자료, 기존 스택과 모바일 요구는 무엇인가?

사용자가 판단을 위임하면 목적에 맞게 가정하고 기록해 진행한다. 답변 대기 중에는 프로젝트 조사·실행 준비처럼 독립적인 작업을 한다. 추정을 사용자가 확인한 사실로 취급하지 않는다.

프로젝트의 AGENTS.md와 해당 도구의 프로젝트 지침을 읽고 기존 스택·컴포넌트·실행 명령을 우선한다. 다른 스킬이 설치돼 있어야만 작동하는 흐름을 만들지 않는다.

## 2. 로컬 자료에서 세 방향 제안

`templates/brief.json` 형식으로 `design/brief.json`을 작성한다. 아래 명령은 네트워크·모델 API를 호출하지 않는다.

```bash
python <skill>/scripts/recommend.py --brief design/brief.json
```

- [스타일 프리셋](references/styles.json)의 색·타이포·반경·실루엣과 [화면 구조](references/layouts.json)를 결합한다.
- 추천 출력과 [사이트·패턴 인덱스](references/library-index.md)에서 후보를 찾고 관련 문서만 읽는다. 모든 사이트를 한 번에 컨텍스트에 넣지 않는다.
- 추천된 `local_image`를 직접 열고 명세와 비교한다. 이미지 열람 기능이 없으면 명세를 사용하고 시각 검증 제약을 알린다.
- `usable: false` 및 `needs-review` 자료는 주 레퍼런스로 선택하지 않는다.
- 세 안은 색뿐 아니라 실루엣·정보 밀도·타이포·이미지 비중·탐색 방식에서 차이를 둔다. 핵심 행동에 적합한 이유와 장단점을 설명한다.
- 추천 점수는 로컬 규칙의 우선순위이며 원본 디자인 품질 점수가 아니다. 스타일 토큰은 독자적인 프리셋으로, 원본에서 측정한 값이 아니다.
- 사용자 선택을 받아 구현한다. 이미 방향을 정했거나 자율 진행을 요청했다면 적합한 안을 택하고 진행한다.

제안과 결정은 `design/ui-proposal.md`에 남긴다. 특정 화면을 사용자에게 소개할 때 명세의 `mobbin_url`도 링크한다. 출처 링크를 여는 것은 오프라인 사용의 조건이 아니다.

## 3. 구현 명세

[패턴별 플레이북](references/playbooks.md)의 해당 항목을 읽고 `design/design-spec.md`에 아래 내용을 정한다.

- 페이지 목적, 섹션 순서, 내비게이션과 핵심 흐름
- 최대 폭, 열 구성, 이미지 비율, 글자 계층과 실제 문구 길이
- 배경·표면·본문·강조 색, 간격·반경·테두리 토큰
- 모바일 재배치, 키보드·초점·터치 동작
- 기본·선택·빈 결과·로딩·오류·완료 상태
- 실제 데이터·API와 로컬 데모의 경계

관찰·사용자 요구·새 구현 제안을 구분한다. 한 섹션을 수집한 사이트를 전체 분석했다고 말하지 않는다. 부족한 화면은 목적에 맞게 설계하되 출처를 지어내지 않는다.

## 4. 실제 구현

[오프라인 구현 지침](references/offline-implementation.md)을 따른다.

- 기존 프로젝트는 기존 스택으로 구현한다. 예제 생성기를 이유로 React·Vue·Svelte 프로젝트를 갈아엎지 않는다.
- 빈 프로젝트에 빠른 동작 예제가 필요하면 생성기를 사용한다. 8개 구조와 18개 스타일을 선택할 수 있다.

```bash
python <skill>/scripts/scaffold.py --brief design/brief.json --output ./prototype
python <skill>/scripts/scaffold.py --brief design/brief.json --style warm-editorial --layout editorial --output ./prototype-editorial
```

- 생성 예제를 사용자 브랜드·콘텐츠·기능으로 발전시킨다. 샘플 문구와 도형만 남긴 화면을 완성품으로 보고하지 않는다.
- 전체 레이아웃 → 타이포·간격 → 색·이미지 → 세부 요소 순으로 구현한다.
- 검색·필터·탭·폼·모달·수량·장바구니·예약·진도 등 필요한 행동을 연결한다. 보이는 버튼을 동작 없이 남기지 않는다.
- API가 없으면 일관된 로컬 데이터로 완주 가능한 흐름을 만든다. 결제·계정·예약·게시가 실제 처리된 것처럼 보이지 않게 데모 완료를 표시한다.
- 레이블·오류·포커스·키보드·대체 텍스트·reduced-motion을 포함한다. 브랜드 색이 대비를 깨면 읽을 수 있는 대체 글자색을 적용한다.
- 사용자 자료가 있으면 활용한다. 원본 로고·고객 후기·상품을 사용자 브랜드의 실제 자료처럼 제시하지 않는다.

## 5. 검증과 전달

[완료 검증표](references/quality-checklist.md)에 따라 프로젝트의 빌드·타입 검사와 주요 흐름을 확인한다. 브라우저가 있으면 최소 375px와 데스크톱에서 겹침·가로 넘침·콘솔 오류·동작을 검증한다. 로컬 원본 비교에는 같은 뷰포트를 사용한다.

구현 파일·화면과 동작·실행 방법·검증 범위·남은 제약을 전달한다. 설계 제안만 작성하고 구현까지 했다고 보고하지 않는다. 배포는 사용자가 요청한 범위에서 진행한다.

## 선택적 자료 확장

기본 작업에는 MCP를 호출하지 않는다. 사용자가 추가 출처를 원하고 도구가 연결됐을 때 [Mobbin MCP 지침](references/mobbin-mcp.md)과 [확장 절차](references/expansion-workflow.md)를 적용한다. 전체 목록을 열거할 도구가 없으면 전수 수집했다고 주장하지 않는다. 수집 상태는 `references/collection-report.json`을 따른다.
