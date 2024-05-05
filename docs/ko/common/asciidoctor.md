---
layout: page
title: common/asciidoctor (한국어)
description: "AsciiDoc 파일을 게시 가능한 형식으로 변환하는 프로세서."
content_hash: a07a5faa872124619ccc26ff8b8fd4a79b6e6295
last_modified_at: 2024-05-05
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

AsciiDoc 파일을 게시 가능한 형식으로 변환하는 프로세서.
더 많은 정보: <https://docs.asciidoctor.org>.

- 특정 `.adoc` 파일을 HTML(기본 출력 형식)로 변환:

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.adoc</span>

- 특정 `.adoc` 파일을 HTML로 변환하고 CSS 스타일시트 연결:

`asciidoctor -a stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스타일시트.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.adoc</span>

- 특정 `.adoc` 파일을 포함 가능한 HTML로 변환하고, 본문을 제외한 모든 항목을 제거:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.adoc</span>

- `asciidoctor-pdf` 라이브러리를 사용하여 특정 `.adoc` 파일을 PDF로 변환:

`asciidoctor --backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.adoc</span>
