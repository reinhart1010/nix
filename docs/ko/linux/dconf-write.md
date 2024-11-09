---
layout: page
title: linux/dconf-write (한국어)
description: "dconf 데이터베이스에 키 값을 작성합니다."
content_hash: 26fc109ce3f0898b4a8b810661ecb7b9ce77d4c4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dconf-write.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dconf-write.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dconf write

dconf 데이터베이스에 키 값을 작성합니다.
같이 보기: `dconf`.
더 많은 정보: <https://manned.org/dconf>.

- 특정 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 특정 문자열 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`'"`

- 특정 정수 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`"`

- 특정 불리언 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>`"`

- 특정 배열 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "[`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'첫번째', '두번째', ...</span>`]"`

- 특정 빈 배열 키 값 작성:

`dconf write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>` "@as []"`
