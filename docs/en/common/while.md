---
layout: page
title: common/while (English)
description: "Simple shell loop."
content_hash: 2dc331e80b2571c7ced27b3b0f65e30ea006a5a4
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
tldri18n_status: 2
---
# while

Simple shell loop.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- Read `stdin` and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; sleep 1; done`
