# Productboard

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## Productboard: 작업 관리 대시보드

- 자료 유형: screen
- 출처: [Productboard — Mobbin](https://mobbin.com/screens/6ca218fe-d545-49fd-abff-a0032ab03d2a)
- 확인 날짜: 2026-10-11
- 패턴: dashboard, task-management

### 직접 관찰

- 좁은 왼쪽 사이드바, 상단 Tasks 헤더와 검색·Create 버튼, 가운데 작업 목록, 오른쪽 상세 패널. 목록 배경은 연한 회색이고 상세 패널은 흰색이다. 상태는 회색·파랑·빨강·노랑·초록 점으로 구분된다.

![Productboard — 참고 화면](../../../assets/references/6ca218fe-d545-49fd-abff-a0032ab03d2a.jpg)


원본 파일: [오프라인 JPEG](../../../assets/references/6ca218fe-d545-49fd-abff-a0032ab03d2a.jpg).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
