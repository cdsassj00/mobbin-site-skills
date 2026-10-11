# Mobbin Site Skills

Mobbin MCP에서 수집한 **121개 사이트의 152개 레퍼런스**를 바탕으로 다양한 웹사이트를 만드는 재사용 스킬.

- 개별 화면 **34개**, 사이트 섹션 **111개**, 사용자 흐름 **7개**
- 원본 이미지 **207장**을 클라우드 `assets/library/`에 다운로드
- 직접 확인한 프리뷰 이미지 **171장**의 관찰 메모
- SaaS·개발자 랜딩, 커머스, 대시보드, 금융, 채용, 여행·식당, 학습·미디어, 포트폴리오·블로그, 팀·후기, 문의·FAQ, 가입·게시용 **11개 구현 플레이북**

이는 Mobbin 전체 사이트의 전수 수집이나 121개 완성 웹앱이 아니다. 수집한 범위의 관찰과 구현 지침이며, 추가 사이트·화면은 스킬 실행 중 MCP로 계속 확장한다. 흐름별 확인한 단계와 판독하기 어려운 자료는 각 명세에 표시했다.

## 바로 사용

```text
skills/mobbin-site-builder/SKILL.md를 읽고 적용해줘.
라이브러리에서 내 서비스에 맞는 레퍼런스를 찾아 SaaS 사이트를 만들어줘.
홈, 요금제, 가입 화면이 필요해. 부족한 화면은 Mobbin MCP로 추가 검색해줘.
```

```text
$mobbin-site-builder
상품 사진이 중심인 쇼핑몰을 만들어줘.
라이브러리의 커머스 자료를 비교하고 갤러리·옵션·장바구니·결제 데모를 연결해줘.
```

[사이트 이름·패턴별 전체 인덱스](skills/mobbin-site-builder/references/library-index.md)에서 레퍼런스를 고를 수 있다. 브랜드와 내용은 사용자 서비스에 맞게 바꾸고, 레퍼런스의 레이아웃과 정보 밀도를 살린다.

## 검색

Python 표준 라이브러리만 사용한다.

```bash
python scripts/search_library.py Linear
python scripts/search_library.py --tag pricing
python scripts/search_library.py --kind flow
python scripts/search_library.py "세리프"
python scripts/search_library.py --tag product-detail --json
```

판독이 어려운 자료는 기본 검색에서 제외한다. 보려면 `--include-needs-review`를 추가한다.

## Codex 설치

```bash
bash scripts/install.sh
# 설치 위치를 직접 지정할 수도 있다.
bash scripts/install.sh /path/to/skills
```

기본 경로는 `${CODEX_HOME:-$HOME/.codex}/skills`다. 이름이 같은 설치가 있으면 덮어쓰지 않는다. 설치 후 새 세션에서 `$mobbin-site-builder`로 호출한다. 설치 없이 파일 경로를 지정해서 적용할 수도 있다. 사이트별 명세와 인덱스는 스킬 폴더에 포함돼 단독 설치 후에도 사용할 수 있다.

## 구성

- `skills/mobbin-site-builder/SKILL.md`: 레퍼런스 선택 → 명세 → 구현 → 검증
- `references/library-index.md`: 사이트·패턴 인덱스
- `references/library.json`: 출처·태그·화면별 관찰을 담은 원본 데이터
- `references/library/sites/`: 121개 사이트별 명세
- `references/playbooks.md`: 패턴별 구현 규칙과 완료 조건
- `references/mobbin-mcp.md`: Mobbin 도구 선택·검색·다운로드 규칙
- `references/expansion-workflow.md`: 새 사이트·화면 추가 방법
- `scripts/`: 검색, 인덱스 재생성, 고해상도 다운로드, 설치
- `templates/`: 개별 사이트를 더 깊이 분석하는 양식

위 `references/` 경로는 `skills/mobbin-site-builder/` 아래에 있다.

## 수집과 확장

MCP의 screens / sections / flows를 실제 호출하고 반환 이미지를 보고 관찰했다. 검색 의도와 실제 화면이 다른 자료는 관찰한 구조로 다시 분류했다. 같은 ID는 중복 제거하되 서로 다른 타이포그래피·버전의 화면은 유지한다.

검색 결과의 이미지 URL은 만료되므로 장기 출처는 `mobbin_url`을 사용한다. 원본 이미지와 임시 다운로드 URL은 Git에서 제외된 클라우드 `assets/`에 보관하고 공개 저장소에는 분석과 출처를 넣는다. 새 클라우드 환경에서는 MCP로 새 다운로드 URL을 얻어 원본을 다시 가져올 수 있다.

```bash
python scripts/build_library.py
python scripts/download_assets.py assets/library-download-manifest.json
```

새 자료 기록의 형식은 [확장 지침](skills/mobbin-site-builder/references/expansion-workflow.md)을 따른다. 직접 확인하지 않은 화면·모바일·전환은 추정으로 구분한다.
