---
layout: page
title: common/cmark (한국어)
description: "CommonMark Markdown 텍스트를 다른 텍스트 형식으로 변환합니다."
content_hash: 00fce0659ba0f89e1570c9e87d3b046c249f6290
related_topics:
  - title: English version
    url: /en/common/cmark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmark.html
    icon: bi bi-globe
---
# cmark

CommonMark Markdown 텍스트를 다른 텍스트 형식으로 변환합니다.
더 많은 정보: <https://github.com/commonmark/cmark>.

- CommonMark Markdown 파일을 HTML 파일로 렌더링합니다:

`cmark --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.md</span>

- 데이터를 표준 입력에서 라텍스로 변환:

`cmark --to latex`

- 직선 따옴표를 스마트 따옴표로 변환:

`cmark --smart --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.md</span>

- UTF-8 문자들을 검증:

`cmark --validate-utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.md</span>
