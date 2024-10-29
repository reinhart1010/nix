---
layout: page
title: common/pdf-parser (한국어)
description: "PDF 파일의 기본 요소를 렌더링 없이 식별."
content_hash: 4cab2f397b582feac4826bf40126b21b766fa113
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/pdf-parser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdf-parser

PDF 파일의 기본 요소를 렌더링 없이 식별.
더 많은 정보: <https://blog.didierstevens.com/programs/pdf-tools>.

- PDF 파일의 통계 표시:

`pdf-parser --stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- PDF 파일에서 `/Font` 유형의 객체 표시:

`pdf-parser --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Font</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 간접 객체에서 문자열 검색:

`pdf-parser --search=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
