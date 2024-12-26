---
layout: page
title: common/while (English)
description: "Simple shell loop that repeats while the return value remains zero."
content_hash: 3b4d3441263155d24a710aeedc12bf613ef16735
last_modified_at: 2024-12-26
related_topics:
  - title: 한국어 version
    url: /ko/common/while.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
tldri18n_status: 2
---
# while

Simple shell loop that repeats while the return value remains zero.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- Read `stdin` and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; sleep 1; done`

- Execute a command until it fails:

`while `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; do :; done`
