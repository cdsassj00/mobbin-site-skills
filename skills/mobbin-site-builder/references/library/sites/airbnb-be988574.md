# Airbnb

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 숙소 예약

- 자료 유형: flow
- 출처: [Airbnb — Mobbin](https://mobbin.com/flows/be988574-2b30-4b82-a5a3-30352abbf1a2)
- 확인 날짜: 2026-10-11
- 패턴: booking, travel

### 직접 관찰

- 단계 1: 왼쪽 두 달 달력의 체크인아웃 선택, 오른쪽 둥근 예약 카드에 가격·날짜·인원·분홍 Reserve. 아래 큰 평점과 Guest favorite.
- 단계 5: 예약 결제수단 단계. 왼쪽 신용카드·PayPal·Apple Pay·Google Pay 라디오와 입력. 카드번호 필드에 빨간 오류. 오른쪽 숙소·취소정책·일정·가격 요약.
- 단계 8: 예약 검토 단계. 앞 단계는 접힌 요약과 Change, 아래 여행보험 체크박스·약관·분홍 Confirm and pay. 오른쪽 예약 요약 유지.
- 단계 12: 완료가 아닌 숙박 승인 대기 상태. 크림 배경 왼쪽 큰 숙소 카드·Pending 배지, 오른쪽 Your stay is pending 설명·검정 Got it.
- 단계 15: Trips 화면. 숙소 가로 카드·도착 안내 타임라인, 아래 활동 추천 이미지 카드. 예약 이후 여정도 분리해서 보여줌.

전체 15단계 중 직접 확인한 단계는 5개다. 확인하지 않은 단계의 상태·전환은 원본을 보고 확정한다.

### 전체 단계의 클라우드 파일

- 1: `assets/library/40cb4148-15dc-414a-8b47-202a039f7e27.jpg`
- 2: `assets/library/54761527-353f-47f1-bcf7-c59d267b0e15.jpg`
- 3: `assets/library/5dae47fd-6764-4452-b208-324c253af5a8.jpg`
- 4: `assets/library/3c76c41f-4239-4487-b0b5-804ad2970a21.jpg`
- 5: `assets/library/1aa397a5-3fea-4548-9980-528eea748d91.jpg`
- 6: `assets/library/8044ef51-b695-433c-8555-da9d4f782e7a.jpg`
- 7: `assets/library/3dd02d92-d632-47b4-b82b-80e8aa53a196.jpg`
- 8: `assets/library/bcd5d2bf-5f5f-4b4b-9967-4fccc6e7450d.jpg`
- 9: `assets/library/be1a3101-2582-45a4-9993-a700bc7b0e44.jpg`
- 10: `assets/library/d5f132b1-8652-4e8d-bcac-c1661350bd05.jpg`
- 11: `assets/library/252a2f97-a9e1-4287-9428-329bb0c23d46.jpg`
- 12: `assets/library/101aa54b-0fc2-4adf-bf46-1bd6ecb620c3.jpg`
- 13: `assets/library/81cb5333-40c3-431b-a728-d2266e728b35.jpg`
- 14: `assets/library/d3a8ceec-6af8-4f17-8e78-a9526936ac10.jpg`
- 15: `assets/library/78bcb64d-290d-45bf-9442-a03361754fcc.jpg`

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
