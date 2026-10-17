# Mercor

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 채용 탐색

- 자료 유형: screen
- 출처: [Mercor — Mobbin](https://mobbin.com/screens/b1527c3a-5d57-4e86-b310-bc6a5b9ec23e)
- 확인 날짜: 2026-10-11
- 패턴: recruitment

### 직접 관찰

- 채용 탐색. 좁은 아이콘 레일, 상단 Resume·Location·Assessment 진행. Project-based 탭·검색·필터 칩·정렬, 세 열 역할 카드와 Domain 드롭다운.

![Mercor — 참고 화면](../../../assets/references/b1527c3a-5d57-4e86-b310-bc6a5b9ec23e.jpg)


원본 파일: [오프라인 JPEG](../../../assets/references/b1527c3a-5d57-4e86-b310-bc6a5b9ec23e.jpg).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
