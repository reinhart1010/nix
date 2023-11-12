---
layout: page
title: linux/pidof (English)
description: "Gets the ID of a process using its name."
content_hash: b2d167b4e7206589ce7ce3bd0c7a0f884ec15edb
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/pidof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pidof

Gets the ID of a process using its name.
More information: <https://manned.org/pidof>.

- List all process IDs with given name:

`pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- List a single process ID with given name:

`pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- List process IDs including scripts with given name:

`pidof -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Kill all processes with given name:

`kill $(pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`)`
