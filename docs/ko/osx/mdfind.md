---
layout: page
title: osx/mdfind (한국어)
description: "쿼리에 맞는 파일 나열."
content_hash: 86329f059509301ea773b44a368d0e32ebde2962
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/mdfind.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mdfind.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mdfind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdfind

쿼리에 맞는 파일 나열.
더 많은 정보: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- 파일 이름으로 찾기:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 파일 내용을 통해 찾기:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`"`

- 특정 디렉토리 내 문자열을 포함하는 파일 찾기:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`"`
