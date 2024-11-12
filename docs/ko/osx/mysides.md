---
layout: page
title: osx/mysides (한국어)
description: "Finder 즐겨찾기 추가, 나열 및 제거 도구."
content_hash: c2778f474812e29f21d8f0251766d1255b71e99c
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/mysides.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mysides.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysides

Finder 즐겨찾기 추가, 나열 및 제거 도구.
더 많은 정보: <https://github.com/mosen/mysides>.

- 사이드바 즐겨찾기 나열:

`mysides list`

- 새로운 항목을 사이드바 즐겨찾기 끝에 추가:

`mysides add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예시</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///Users/Shared/example</span>

- 이름으로 항목 제거:

`mysides remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예시</span>

- 현재 디렉토리를 사이드바에 추가:

`mysides add $(basename $(pwd)) file:///$(pwd)`

- 현재 디렉토리를 사이드바에서 제거:

`mysides remove $(basename $(pwd))`
