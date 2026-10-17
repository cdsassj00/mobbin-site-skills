# 오프라인 구현

이 스킬은 Mobbin 구독·MCP·API 키·인터넷 없이 브리프 질문, 추천, 이미지 열람, UI 생성까지 가능하다. 에이전트 자체 실행에 필요한 모델 연결은 사용 환경의 조건이다.

## 설치 폴더에 포함된 것

- `references/library.json`, `references/library-index.md`, `references/library/sites/`: 분석 명세와 출처
- `assets/references/`: 다운로드한 실제 JPEG 레퍼런스. Mobbin 워터마크를 유지한다.
- `references/styles.json`: 독자적으로 설계한 스타일 프리셋. 원본 사이트에서 측정한 토큰으로 표시하지 않는다.
- `references/layouts.json`: 목적별 페이지 구성과 핵심 동작
- `scripts/recommend.py`: 목적·스타일 기반 로컬 추천
- `scripts/scaffold.py`, `assets/starter/`: 외부 의존성이 없는 동작 예제 생성

## 사용 순서

1. 인터뷰 결과로 브리프를 작성한다.
2. 추천 도구로 3개 방향을 고르고 각 방향의 사이트 명세와 실제 로컬 이미지를 연다.
3. 이미지에서 확인한 사실과 독자적인 구현 규칙을 구분해 명세로 만든다.
4. 기존 코드가 있으면 그 스택으로 구현한다. 새 프로젝트의 빠른 시작은 아래 생성기를 쓴다.

```bash
python <skill>/scripts/recommend.py --brief design/brief.json
python <skill>/scripts/scaffold.py --brief design/brief.json --output ./prototype
python -m http.server 8000 --directory ./prototype
```

`--style`과 `--layout`으로 방향을 지정할 수 있다. 출력 폴더가 비어 있지 않으면 생성기는 덮어쓰지 않는다. 실행 가능한 시작점이며 제품의 실제 데이터·API·브랜드 콘텐츠는 후속 구현으로 연결한다.

## 도구가 제한된 에이전트

Python이 없으면 JSON·마크다운을 직접 읽고 제공된 CSS·HTML·JS를 기존 프레임워크에 옮긴다. 이미지 열람 기능이 없으면 관찰 명세로 진행하고 그 검증 제약을 알린다. MCP나 이미지 업로드를 사용자에게 필수 준비물로 요구하지 않는다.

## 추가 온라인 수집

사용자가 새 출처나 특정 사이트를 원하고 MCP가 연결돼 있을 때만 [Mobbin MCP 지침](mobbin-mcp.md)을 사용한다. 기존 자료를 활용하는 기본 흐름에는 호출하지 않는다. 자료의 수집·확인 범위는 `references/collection-report.json`을 따른다.
