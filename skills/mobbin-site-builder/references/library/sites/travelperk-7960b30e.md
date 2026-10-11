# TravelPerk

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## TravelPerk: 3단 요금제 사이트

- 자료 유형: section
- 출처: [TravelPerk — Mobbin](https://mobbin.com/sites/sections/7960b30e-a40a-4ef8-b4e2-89d4c80cb113)
- 확인 날짜: 2026-10-11
- 패턴: pricing

### 직접 관찰

- 밝은 배경 위 Plans that get you places 제목과 Starter / Premium / Pro 세 카드. Starter는 흰 바탕에 테두리, 나머지는 연한 크림색이다. Premium 제목 옆 하늘색 Most Popular 배지. 가격은 큰 검정 글자, CTA는 외곽선 또는 라임색이다.

원본 파일: `assets/library/7960b30e-a40a-4ef8-b4e2-89d4c80cb113.jpg` (Git 제외).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
