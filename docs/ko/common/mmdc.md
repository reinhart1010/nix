---
layout: page
title: common/mmdc (한국어)
description: "도메인 특화 언어를 사용하는 다이어그램 생성 도구인 mermaid의 CLI."
content_hash: 3db4d8a1d178bd6d98fbaa47fcf8eb1a202ba7eb
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mmdc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mmdc

도메인 특화 언어를 사용하는 다이어그램 생성 도구인 mermaid의 CLI.
mermaid 정의 파일을 입력으로 받아 SVG, PNG 또는 PDF 파일을 출력으로 생성.
더 많은 정보: <https://mermaid-js.github.io/mermaid/>.

- 파일을 지정된 형식으로 변환 (파일 확장자에 따라 자동 결정):

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.svg</span>

- 차트의 테마 지정:

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.svg</span>` --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">forest|dark|neutral|default</span>

- 차트의 배경색 지정 (예: `lime`, `"#D8064F"` 또는 `transparent`):

`mmdc --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mmd</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.svg</span>` --backgroundColor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>
