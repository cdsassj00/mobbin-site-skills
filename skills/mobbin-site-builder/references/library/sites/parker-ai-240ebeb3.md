# Parker AI

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 짙은 초록 바탕의 가격 안내. 왼쪽 큰 포함 기능 카드, 오른쪽 Starter·Growth 카드 세로 배치와

- 자료 유형: section
- 출처: [Parker AI — Mobbin](https://mobbin.com/sites/sections/240ebeb3-dfb9-4fe3-8bc0-9f069adab348)
- 확인 날짜: 2026-10-18
- 패턴: pricing

### 직접 관찰

- 짙은 초록 바탕의 가격 안내. 왼쪽 큰 포함 기능 카드, 오른쪽 Starter·Growth 카드 세로 배치와 검정 CTA.

![Parker AI — 참고 화면](../../../assets/references/240ebeb3-dfb9-4fe3-8bc0-9f069adab348.jpg)


원본 파일: [오프라인 JPEG](../../../assets/references/240ebeb3-dfb9-4fe3-8bc0-9f069adab348.jpg).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
