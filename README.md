# Offline UI Designer & Builder

**Mobbin MCP 없이 목적을 질문하고, UI 방향을 제안하고, 실제 사이트를 구현하는 멀티 에이전트 스킬.**

Claude Code · Codex · OpenCode · Grok Build에서 같은 스킬과 로컬 자료를 사용한다. Mobbin 구독이나 API 키가 필요 없다.

## 설치

```bash
git clone https://github.com/cdsassj00/mobbin-site-skills.git
cd mobbin-site-skills
python scripts/install.py --agent claude --global
# 사용하는 도구에 맞게 claude를 codex / opencode / grok으로 변경
```

프로젝트 한 곳에만 설치하려면:

```bash
python scripts/install.py --agent codex --project /path/to/project
# 여러 도구를 같은 프로젝트에서 사용하는 경우
python scripts/install.py --agent all --project /path/to/project
```

설치에는 Python 3.9 이상이 필요하다. 스킬 폴더를 해당 도구의 skills 디렉터리에 직접 복사해도 된다. 기존 파일은 덮어쓰지 않는다. 이 설치기가 만든 버전은 `--replace`로 백업 후 갱신한다. [에이전트별 경로와 공식 문서](docs/AGENT-COMPATIBILITY.md)를 확인할 수 있다.

ZIP으로 받으려면 [릴리스](https://github.com/cdsassj00/mobbin-site-skills/releases/latest)에서 스킬 단독 패키지 또는 설치기 포함 툴킷을 다운로드한다. 스킬 ZIP에는 이미지·명세·예제가 모두 포함된다.

## 사용

Claude Code와 Grok Build에서는 `/mobbin-site-builder`, Codex에서는 `$mobbin-site-builder`로 요청한다. OpenCode에서는 이 스킬을 사용해 달라고 자연어로 요청한다. 도구의 스킬 목록에서 선택해도 된다.

```text
이 스킬로 내 사이트를 만들어줘.
먼저 사이트 목적, 사용자, 디자인풍과 스타일을 물어보고
맞는 UI 방향 3개를 제안해줘. 선택한 방향으로 구현까지 해줘.
```

스킬의 기본 흐름:

1. 목적·대상·핵심 행동, 디자인풍, 페이지·기능을 질문한다.
2. 로컬 자료에서 구조와 분위기가 다른 세 방향을 제안한다.
3. 선택한 방향의 토큰·반응형·상태·사용자 흐름을 명세로 만든다.
4. 기존 프로젝트의 스택 또는 독립 실행 예제로 구현한다.
5. 핵심 동작과 모바일·데스크톱을 검증한다.

이미 답한 내용은 반복해서 묻지 않는다. 사용자가 자율 진행을 요청하면 가정을 기록하고 적합한 방향으로 진행한다. Mobbin MCP는 새 자료를 추가할 때만 선택적으로 사용한다.

## 들어 있는 자료

| 구성 | 범위 |
| --- | ---: |
| 출처 사이트 | 193개 |
| 화면·섹션·흐름 명세 | 295개 |
| 설치 폴더에 포함된 원본 JPEG | 350장 |
| 직접 본 프리뷰·연락판 이미지의 관찰 | 314개 |
| 독자적인 스타일 프리셋 | 18종 |
| 동작하는 UI 시작 구조 | 8종 |
| 패턴별 구현 플레이북 | 11개 |

[전체 사이트·패턴 인덱스](skills/mobbin-site-builder/references/library-index.md) · [수집 범위 기록](skills/mobbin-site-builder/references/collection-report.json) · [자료 출처](NOTICE.md)

원본 이미지는 `skills/mobbin-site-builder/assets/references/`에 포함된다. 다른 사람이 MCP 없이 직접 보고 참고할 수 있다. 만료되는 이미지 다운로드 URL은 공개 데이터에 넣지 않는다.

**Mobbin 전체를 전수 수집한 결과는 아니다.** 연결된 도구는 검색 3종뿐이며 전체 카탈로그 열거·전체 내보내기를 제공하지 않는다. 추가 수집 중 요청 제한이 발생했고, 미방문 페이지·미확인 자료를 확보한 것으로 계산하지 않았다. 한 섹션을 확인한 것을 전체 사이트 분석으로 표시하지 않는다. 판독하기 어려운 10개 자료는 기본 추천에서 제외한다.

## 오프라인 추천과 생성

외부 패키지·모델 API 없이 Python 표준 라이브러리로 실행한다.

```bash
cp skills/mobbin-site-builder/templates/brief.json brief.json
# brief.json에 목적, 대상, 핵심 행동, 선호 스타일 등을 입력
python skills/mobbin-site-builder/scripts/recommend.py --brief brief.json
python skills/mobbin-site-builder/scripts/scaffold.py --brief brief.json --output ./prototype
python -m http.server 8000 --directory ./prototype
```

특정 구조와 스타일을 선택할 수도 있다.

```bash
python skills/mobbin-site-builder/scripts/scaffold.py --brief brief.json \
  --layout commerce --style luxury-minimal --output ./shop
```

8개 구조는 랜딩, 대시보드, 쇼핑, 편집 콘텐츠, 포트폴리오, 예약, 학습, 디렉터리다. 검색·필터·상품 상세·수량·장바구니 합계·날짜 검증·진도·폼 검증 등 해당 구조의 핵심 동작을 포함한다. 실제 결제·예약·회원가입·전송은 수행하지 않는 데모다. 사용자 서비스에 맞는 데이터·브랜드·기능을 추가해 완성하는 시작점이다.

18개 스타일은 정돈된 제품형, 따뜻한 편집형, 어두운 기술형, 선명한 커머스, 절제된 프리미엄, 유쾌한 스튜디오, 차분한 케어, 밀도 높은 업무형, 자연스러운 생활형, 흑백 포트폴리오, 부드러운 제품형, 대담한 타이포형, 금융형, 사진 중심 여행형, 커뮤니티형, 학습형, 정밀한 격자형, 기업 신뢰형이다. 토큰과 시작 코드는 독자적인 구현 프리셋이며 원본 사이트의 측정값·소스코드가 아니다.

## 검색·검증·패키징

```bash
python scripts/search_library.py --tag pricing
python scripts/search_library.py Linear
python scripts/search_library.py --kind flow
python scripts/build_library.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/package.py
```

브라우저 검증은 [검증 기록](docs/VALIDATION.md)에 정리했다. 에이전트별 경로 설치 검증과 각 제품의 실제 모델 세션 검증은 구분한다.

## 폴더

- `skills/mobbin-site-builder/`: 단독 설치 가능한 스킬 전체
- `references/intake.md`: 목적·스타일 인터뷰와 UI 제안 방식
- `references/styles.json`, `layouts.json`: 스타일·구조 데이터
- `references/library.json`, `library/sites/`: 관찰과 출처
- `assets/references/`: 실제 참고 이미지
- `assets/starter/`, `scripts/`: 오프라인 동작 예제와 추천기
- 저장소의 `scripts/`: 설치·검색·자료 생성·패키징

위 references·assets 경로는 스킬 폴더 아래에 있다. 기본 사용에는 네트워크가 필요 없으며, 에이전트 자체 모델 연결 조건은 사용 도구에 따른다.
