# 라이브러리 확장

현재 수집한 사이트에만 제한하지 않는다. 사용자 요청에 적합한 자료가 없거나 일부 단계만 확인됐다면 Mobbin MCP로 새 자료를 찾아 구현 지침을 추가한다.

1. 기존 인덱스·태그·사이트 문서를 검색한다. 주요 레퍼런스 후보는 `usable: true` 자료에서 고른다.
2. 단일 의도의 구체적인 검색문으로 screens / sections / flows를 호출한다. 필요한 경우 페이지를 넘기거나 서비스명을 지정한다.
3. 반환 이미지를 직접 확인한다. 검색어와 실제 UI가 다르면 관찰한 UI로 분류한다. 같은 ID는 중복 등록하지 않는다.
4. 프리뷰 관찰은 프리뷰 관찰로 표시한다. 고해상도 이미지·모바일 화면·미확인 흐름 단계를 추가로 확인한 경우에만 확인 범위를 넓힌다.
5. `references/library.json`에 아래 형식으로 기록한다. `image_url`은 만료되므로 공개 데이터에 넣지 않는다.
6. 원본 다운로드용 URL은 Git 제외 경로 `assets/library-download-manifest.json`에 `{id, image_url}`로 저장하고 `python scripts/download_assets.py assets/library-download-manifest.json`을 실행한다.
7. 저장소에서 `python scripts/build_library.py`를 실행해 사이트 명세·통계·인덱스를 재생성한다.

```json
{
  "id": "Mobbin result ID",
  "site": "Observed service name",
  "kind": "screen",
  "title": "실제 화면 유형",
  "mobbin_url": "https://mobbin.com/screens/<id>",
  "tags": ["product-detail", "commerce"],
  "usable": true,
  "queries": ["original query"],
  "observations": [
    {"screen_id": "screen ID", "note": "직접 본 구조와 요소"}
  ]
}
```

흐름은 `kind: flow`, `screen_count`, `screens: [{id, position}]`를 추가하고 각 observation에 position을 기록한다. 직접 보지 않은 단계는 observations에 넣지 않는다. 판독하기 어려운 자료는 `usable: false`와 `needs-review` 태그로 남긴다.

## 전체 사이트 구현에 쓸 때

한 섹션을 수집했다고 해당 사이트 전체를 분석한 것은 아니다. 전체 사이트를 요청받으면 홈의 다른 섹션·하위 페이지·핵심 여정·모바일을 추가 검색한다. 관찰된 스타일을 바탕으로 추가한 페이지는 구현 제안으로 표시한다.
