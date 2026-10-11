# lululemon

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 상품 구매

- 자료 유형: flow
- 출처: [lululemon — Mobbin](https://mobbin.com/flows/0a9a45a0-7b9c-4e1c-b838-faa75bd1e3ed)
- 확인 날짜: 2026-10-11
- 패턴: checkout, commerce

### 직접 관찰

- 단계 1: 왼쪽 장바구니 상품행·수량·저장수정삭제, 오른쪽 주문 요약·소계배송세금총액·빨간 Checkout와 PayPal 버튼.
- 단계 3: 중앙 Checkout 진행표시 Contact→Shipping→Payment→Review. 왼쪽 배송 주소 폼, 오른쪽 상품·가격 요약. 연락정보는 접힌 완료 요약.
- 단계 5: 배송 정보 완료 후 Payment 선택 영역. 기프트 카드·Apple Pay·PayPal·Afterpay 등의 가로 아코디언 행. 오른쪽 주문 요약 유지.

전체 5단계 중 직접 확인한 단계는 3개다. 확인하지 않은 단계의 상태·전환은 원본을 보고 확정한다.

### 전체 단계의 클라우드 파일

- 1: `assets/library/4fd7f773-3297-4bdc-b281-61b188f23273.jpg`
- 2: `assets/library/7a884722-b8f4-4d13-be72-c8eba5281937.jpg`
- 3: `assets/library/433eb858-1742-48f6-8f13-7b8a282693dc.jpg`
- 4: `assets/library/6ee844eb-9b49-4f98-8c59-f8a27f7a6c9f.jpg`
- 5: `assets/library/e0b7545c-852b-43ca-90e8-cb0a10d2666f.jpg`

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
