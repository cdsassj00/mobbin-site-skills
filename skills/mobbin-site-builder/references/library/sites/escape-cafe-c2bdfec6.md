# Escape Cafe

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 세로 커머스 카탈로그. 위 큰 ALL PRODUCTS, 서로 다른 크기 상품과 풍경 이미지를 혼합한 편집 그

- 자료 유형: section
- 출처: [Escape Cafe — Mobbin](https://mobbin.com/sites/sections/c2bdfec6-82d4-4e22-baaa-5f866e5c7cdf)
- 확인 날짜: 2026-10-18
- 패턴: commerce

### 직접 관찰

- 세로 커머스 카탈로그. 위 큰 ALL PRODUCTS, 서로 다른 크기 상품과 풍경 이미지를 혼합한 편집 그리드.

![Escape Cafe — 참고 화면](../../../assets/references/c2bdfec6-82d4-4e22-baaa-5f866e5c7cdf.jpg)


원본 파일: [오프라인 JPEG](../../../assets/references/c2bdfec6-82d4-4e22-baaa-5f866e5c7cdf.jpg).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
