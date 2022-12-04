---
layout: page
title: common/while (English)
description: "Simple shell loop."
content_hash: ab93c6be30849d3de82de2833b89181e975300b9
last_modified_at: 2022-12-04
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
---
# while

Simple shell loop.
More information: <https://manned.org/while>.

- Read `stdin` and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; sleep 1; done`
