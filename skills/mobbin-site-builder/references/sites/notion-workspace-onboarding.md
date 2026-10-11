# Notion: 워크스페이스 온보딩

## 출처와 확인 범위

- 확인 날짜: 2026-10-11
- 수집: Mobbin MCP, web
- 직접 관찰: MCP 인라인 프리뷰. 고해상도 원본 파일은 별도 저장.
- https://mobbin.com/flows/757b6888-6eaa-498d-9b18-c013c9a2ef4a

## 관찰

14단계 흐름 중 도구 프리뷰의 1·4·8·11·14번 이미지를 직접 확인했다. 1번은 사이드바와 Getting Started 문서, 4번은 팀·개인·학교 용도 선택 카드, 8번은 워크스페이스 생성 폼 위 로딩 오버레이, 11번은 이메일 초대 폼과 공유 링크·도메인 허용 체크박스, 14번은 팀 워크스페이스의 Getting Started 문서다.

## 구현 명세

- 구성 요소: UsageChoice / WorkspaceForm / LoadingOverlay / InviteForm / WorkspaceShell
- 동작 제안: 용도 선택 → 워크스페이스 이름 → 생성 중 → 초대 또는 건너뛰기 → 시작 문서 흐름은 구현 제안이다. 정확한 14단계 전환은 전체 원본 확인 후 확정한다.
- 시각 규칙: 중앙 좁은 폼과 넓은 여백, 약한 테두리, 파란 CTA를 유지한다. 원본 일러스트는 확보된 자체 에셋으로 교체한다.
- 반응형 제안 (모바일 원본 미확인): 모바일은 선택 카드를 세로로 정리하고 폼은 좌우 여백을 둔 전체 폭으로 표시한다.

## 완료 조건

핵심 행동을 조작할 수 있고, 선택 상태와 빈 결과를 처리하며, 데스크톱 레이아웃을 출처와 비교한다. 정확한 색상·폰트·치수는 고해상도 원본에서 측정 후 확정한다.

## 클라우드 원본 파일 (Git 제외)

- `assets/onboarding/a3c0ef5e-3fbb-42da-bf54-cb022b030f69.jpg` (단계 1)
- `assets/onboarding/bdcaeba0-defc-4abf-837a-7b0b3bfbb24c.jpg` (단계 2)
- `assets/onboarding/6cd8e30a-84d0-4a04-8137-584ac6a0ecb9.jpg` (단계 3)
- `assets/onboarding/d4eda6ca-b6e9-44d4-8c77-f3c91e97b55d.jpg` (단계 4)
- `assets/onboarding/ad74a5b4-deed-40de-b010-1f88afd817a7.jpg` (단계 5)
- `assets/onboarding/aafe4d3c-b61b-482f-8a3d-8e9485e284fe.jpg` (단계 6)
- `assets/onboarding/9f844152-5450-405f-8454-a1708ff89580.jpg` (단계 7)
- `assets/onboarding/97f5505f-120b-49e8-a6a0-b48be692a3d0.jpg` (단계 8)
- `assets/onboarding/7293aa16-d6b2-4611-958e-9f1c7a24a11d.jpg` (단계 9)
- `assets/onboarding/cf470771-b938-4a47-b25e-a332339db93c.jpg` (단계 10)
- `assets/onboarding/a1c40848-1b14-46fe-83ad-e48660fe1dbb.jpg` (단계 11)
- `assets/onboarding/26f5a317-de54-445e-9aba-8058041fcdab.jpg` (단계 12)
- `assets/onboarding/f0053c4d-b614-401d-ac06-44c0b97dcdff.jpg` (단계 13)
- `assets/onboarding/2641304f-d69f-4644-bccc-bc2577f00dc3.jpg` (단계 14)
