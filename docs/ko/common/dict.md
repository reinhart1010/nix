---
layout: page
title: common/dict (한국어)
description: "DICT 프로토콜을 사용하는 명령줄 사전."
content_hash: 94eadbbf8fede37b197ac6a6623619ea3dbde6e5
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dict.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dict

DICT 프로토콜을 사용하는 명령줄 사전.
더 많은 정보: <https://github.com/cheusov/dictd>.

- 사용 가능한 데이터베이스 목록 나열:

`dict -D`

- 데이터베이스에 대한 정보 얻기:

`dict -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 특정 데이터베이스에서 단어를 검색:

`dict -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>

- 사용 가능한 모든 데이터베이스에서 단어를 검색:

`dict `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>

- DICT 서버에 대한 정보 표시:

`dict -I`
