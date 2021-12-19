---
layout: page
title: linux/pidof (English)
description: "Gets the ID of a process using its name."
content_hash: e09417494aa04f197ce042e5619622b23bec47e3
related_topics:
  - title: italiano version
    url: /it/linux/pidof.html
    icon: bi bi-globe
---
# pidof

Gets the ID of a process using its name.

- List all process IDs with given name:

`pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- List a single process ID with given name:

`pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- List process IDs including scripts with given name:

`pidof -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Kill all processes with given name:

`kill $(pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`)`
