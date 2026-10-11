# TravelPerk: 3단 요금제 사이트

## 출처와 확인 범위

- 확인 날짜: 2026-10-11
- 수집: Mobbin MCP, web
- 직접 관찰: MCP 인라인 프리뷰. 고해상도 원본 파일은 별도 저장.
- https://mobbin.com/sites/sections/7960b30e-a40a-4ef8-b4e2-89d4c80cb113

## 관찰

밝은 배경 위 Plans that get you places 제목과 Starter / Premium / Pro 세 카드. Starter는 흰 바탕에 테두리, 나머지는 연한 크림색이다. Premium 제목 옆 하늘색 Most Popular 배지. 가격은 큰 검정 글자, CTA는 외곽선 또는 라임색이다.

## 구현 명세

- 구성 요소: PricingHeader / PlanCard / PopularBadge / PlanCTA / PricingFootnote
- 동작 제안: 요금제 선택 시 해당 플랜을 담아 가입 또는 데모 신청 화면으로 이동한다.
- 시각 규칙: 카드 수, 가격 위계, 설명의 줄 수, CTA 위치를 비교한다. 원본 가격은 참고 자료이며 사용자 가격으로 교체한다.
- 반응형 제안 (모바일 원본 미확인): 모바일은 Starter → Premium → Pro 순서로 한 열 배치한다.

## 완료 조건

핵심 행동을 조작할 수 있고, 선택 상태와 빈 결과를 처리하며, 데스크톱 레이아웃을 출처와 비교한다. 정확한 색상·폰트·치수는 고해상도 원본에서 측정 후 확정한다.

## 클라우드 원본 파일 (Git 제외)

- `assets/pricing/7960b30e-a40a-4ef8-b4e2-89d4c80cb113.jpg`
