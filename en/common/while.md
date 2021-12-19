---
layout: page
title: common/while (English)
description: "Simple shell loop."
content_hash: f370ac3bee4b656eb29f6db9f77b8c2e2bccd827
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
---
# while

Simple shell loop.

- Read stdin and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; sleep 1; done`
