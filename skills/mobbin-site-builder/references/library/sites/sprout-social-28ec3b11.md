# Sprout Social

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## FAQ

- 자료 유형: section
- 출처: [Sprout Social — Mobbin](https://mobbin.com/sites/sections/28ec3b11-74a4-4871-9ec2-8d40d5eec120)
- 확인 날짜: 2026-10-11
- 패턴: faq

### 직접 관찰

- 흰 바탕 파랑 FAQ 배지와 우측 Expand all. 큰 테두리 카드 세 개, 첫 카드 펼쳐짐. 질문 굵은 글자·chevron.

![Sprout Social — 참고 화면](../../../assets/references/28ec3b11-74a4-4871-9ec2-8d40d5eec120.jpg)


원본 파일: [오프라인 JPEG](../../../assets/references/28ec3b11-74a4-4871-9ec2-8d40d5eec120.jpg).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
