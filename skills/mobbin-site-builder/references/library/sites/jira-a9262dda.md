# Jira

이 문서는 수집한 화면·섹션·흐름의 구현 참고 명세다. 전체 사이트 분석을 뜻하지 않는다.

## 가입·인증

- 자료 유형: flow
- 출처: [Jira — Mobbin](https://mobbin.com/flows/a9262dda-0fb7-4350-ac55-a9b8b1a5b29c)
- 확인 날짜: 2026-10-11
- 패턴: authentication, onboarding

### 직접 관찰

- 단계 1: 연한 파랑 랜딩 왼쪽 큰 AI 소개 제목, 오른쪽 이메일 입력·파란 가입·Google 버튼. 아래 네 사용 사례 제품 카드.

![Jira — 참고 화면](../../../assets/references/c0159c8e-dba3-4607-b32d-11d6cdb83a3c.jpg)

- 단계 4: 흰 바탕 중앙 좁은 Atlassian 가입 카드. 이메일·약관·파란 가입 버튼·네 소셜 로그인·기존 계정 링크, 양하단 컬러 일러스트.

![Jira — 참고 화면](../../../assets/references/c406d853-7b88-4e60-98e0-3b5474af04ab.jpg)

- 단계 7: 이메일 인증 완료 후 가입 마무리 카드. 인증 표시·이메일 요약·이름과 비밀번호 입력·보기 토글·8자 안내·파란 Continue.

![Jira — 참고 화면](../../../assets/references/2c586313-8605-4bc2-a44d-66967cf6e476.jpg)

- 단계 10: 가입 후 랜딩으로 돌아온 상태. AI 소개 및 가입 입력은 유지되지만 상단 로그인 링크 대신 사용자 아바타·이름·알림이 보임.

![Jira — 참고 화면](../../../assets/references/e4c04743-5bbf-4df0-87a1-77b9170ded34.jpg)


전체 10단계 중 직접 확인한 단계는 4개다. 확인하지 않은 단계의 상태·전환은 원본을 보고 확정한다.

### 전체 단계의 클라우드 파일

- 1: [로컬 원본](../../../assets/references/c0159c8e-dba3-4607-b32d-11d6cdb83a3c.jpg)
- 2: [로컬 원본](../../../assets/references/e2d2bf98-cd9d-433a-8ce2-6018d122e5ef.jpg)
- 3: [로컬 원본](../../../assets/references/47547f82-1cea-43cf-87f9-7fbf714df905.jpg)
- 4: [로컬 원본](../../../assets/references/c406d853-7b88-4e60-98e0-3b5474af04ab.jpg)
- 5: [로컬 원본](../../../assets/references/fb4d4d6b-a80c-4c8a-8af8-7b5f6e0ec9b9.jpg)
- 6: [로컬 원본](../../../assets/references/2b237a14-d128-4d19-8ff9-6b1d270820cc.jpg)
- 7: [로컬 원본](../../../assets/references/2c586313-8605-4bc2-a44d-66967cf6e476.jpg)
- 8: [로컬 원본](../../../assets/references/155746b6-2e23-4097-a015-0f0485eace48.jpg)
- 9: [로컬 원본](../../../assets/references/2a4972dc-a9a0-40a1-bf81-7bbfe29d896b.jpg)
- 10: [로컬 원본](../../../assets/references/e4c04743-5bbf-4df0-87a1-77b9170ded34.jpg)

### 구현에 적용

- 위 관찰의 열 구성, 이미지 비중, 제목 위계, 색 대비를 먼저 구현한다.
- 화면에 보이는 입력·선택·필터·이동 요소를 실제 동작으로 연결한다. 정적 이미지로 확인되지 않는 동작은 구현 제안으로 기록한다.
- 해당 패턴의 [구현 플레이북](../../playbooks.md)을 읽고 완료 조건을 적용한다.
- 모바일 구성과 정확한 토큰은 이 자료만으로 확정하지 않는다. 모바일 자료를 추가 검색하고 고해상도 원본에서 측정한다.
