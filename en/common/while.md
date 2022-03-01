---
layout: page
title: common/while (English)
description: "Simple shell loop."
content_hash: 105304909b644f36740331f30fffc877f76801e2
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/while.html
    icon: bi bi-globe
---
# while

Simple shell loop.
More information: <https://manned.org/while>.

- Read stdin and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`; sleep 1; done`
