---
layout: page
title: common/daps (한국어)
description: "DocBook XML을 HTML 또는 PDF와 같은 출력 형식으로 변환하기 위한 오픈소스 프로그램."
content_hash: ede5c143d02f4f053e990ec4f9a48f95e86ad8e3
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/daps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/daps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daps

DocBook XML을 HTML 또는 PDF와 같은 출력 형식으로 변환하기 위한 오픈소스 프로그램.
더 많은 정보: <https://opensuse.github.io/daps/doc/index.html>.

- DocBook XML 파일이 유효한지 확인:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>` validate`

- DocBook XML 파일을 PDF로 변환:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>` pdf`

- DocBook XML 파일을 단일 HTML file로 뱐환:

`daps -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>` html --single`

- 도움말 표시:

`daps --help`

- 버전 정보 표시:

`daps --version`
