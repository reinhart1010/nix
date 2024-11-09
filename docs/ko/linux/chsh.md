---
layout: page
title: linux/chsh (한국어)
description: "사용자의 로그인 셸 변경."
content_hash: 9b4f87785791ec513595a0f234882d2ea3839b32
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chsh

사용자의 로그인 셸 변경.
`util-linux`의 일부.
더 많은 정보: <https://manned.org/chsh>.

- 현재 사용자에 대해 특정 로그인 셸을 대화식으로 설정:

`chsh`

- 현재 사용자에 대해 특정 로그인 [s]셸 설정:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>

- 특정 사용자에 대해 로그인 [s]셸 설정:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용 가능한 셸 [l]나열:

`chsh --list-shells`
