# Better Stack

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 제품 랜딩

- 자료 유형: section
- 출처: [Better Stack — Mobbin](https://mobbin.com/sites/sections/56c3bc9d-a358-4878-ba6b-0989d6eef012)
- 확인 날짜: 2026-10-11
- 패턴: saas-landing

### 직접 관찰

- 거의 검정 남색 바탕 중앙 로고·큰 흰 두 줄 제목·보조문·보라 가입 CTA·데모 링크. 주변 어두운 그래프 카드가 떠 있음.

원본 파일: `assets/library/56c3bc9d-a358-4878-ba6b-0989d6eef012.jpg` (Git 제외).

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.

## 구독 업그레이드

- 자료 유형: flow
- 출처: [Better Stack — Mobbin](https://mobbin.com/flows/fdae4948-435d-4760-a192-72c147300b97)
- 확인 날짜: 2026-10-11
- 패턴: billing, subscription

### 직접 관찰

- 단계 1: 짙은 남색 Billing 설정. 왼쪽 설정 사이드바, 본문 설명과 선택 옵션 두 열. 응답자 라이선스 수 슬라이더·지역 선택·선불 번들 라디오 카드.
- 단계 4: 짙은 남색 신용카드 입력 화면. 넓은 카드의 왼쪽 카드 입력, 오른쪽 총액·보라 Pay. 아래 청구서 설정 접힘 링크.
- 단계 8: 청구 정보 확장 상태. 왼쪽 설명, 오른쪽 개인/회사 라디오와 이름·이메일·주소·국가·세금번호·메모 폼. 두 열 입력과 어두운 표면.
- 단계 11: 구독 활성화 결과. 초록 성공 배너, 현재 플랜·청구정보·다음 결제 세 카드, 아래 청구서 표. Change plan·Cancel·Manage credit cards 링크.

전체 11단계 중 직접 확인한 단계는 4개다. 확인하지 않은 단계의 상태·전환은 원본을 보고 확정한다.

### 전체 단계의 클라우드 파일

- 1: `assets/library/d6ae9202-4aac-4e1b-bb3f-a0c9a10fc59e.jpg`
- 2: `assets/library/576c735c-1b82-433a-a80b-e45dcf7ad1bb.jpg`
- 3: `assets/library/28f225a4-c6b0-4afd-ba0c-45ee018d7d01.jpg`
- 4: `assets/library/a2b4260c-2bf8-4e68-b82c-a3b82a27116b.jpg`
- 5: `assets/library/ecf28d9e-e891-425a-b224-452a0925e819.jpg`
- 6: `assets/library/2e3ba128-d0b2-4e40-b0b2-aac31d81bc95.jpg`
- 7: `assets/library/45f0d538-773f-4db1-8ede-aebc292f4a56.jpg`
- 8: `assets/library/b775c3b4-1498-419b-8df7-df4080ad53df.jpg`
- 9: `assets/library/10d44a7b-6b45-4bf5-b707-d98080075e06.jpg`
- 10: `assets/library/93e51d5d-4fd0-4282-b1fb-13d0c1c2f7b3.jpg`
- 11: `assets/library/6e426a2b-e22d-429e-a0a6-81efc8c75d3e.jpg`

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
