---
layout: page
title: common/tmsu (한국어)
description: "파일에 태그를 붙이는 간단한 명령줄 도구."
content_hash: ba56f431036383d33e72bcec544a5976f0bc8cd6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tmsu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmsu

파일에 태그를 붙이는 간단한 명령줄 도구.
더 많은 정보: <https://tmsu.org>.

- 특정 파일에 여러 태그 추가:

`tmsu tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big-jazz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mp3</span>

- 여러 파일에 태그 추가:

`tmsu tag --tags "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music mp3</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- 지정된 파일의 태그 나열:

`tmsu tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- 지정된 태그가 있는 파일 나열:

`tmsu files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big-jazz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">music</span>

- 논리 표현식과 일치하는 태그가 있는 파일 나열:

`tmsu files "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(year >= 1990 and year <= 2000)</span>` and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grunge</span>`"`

- 기존 디렉토리에 tmsu 가상 파일 시스템 마운트:

`tmsu mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
