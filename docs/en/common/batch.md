---
layout: page
title: common/batch (English)
description: "Execute commands at a later time when the system load levels permit."
content_hash: bf552c062d52116322cb1b3c32ff8bd2312c8e7b
related_topics:
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
---
# batch

Execute commands at a later time when the system load levels permit.
Service atd (or atrun) should be running for the actual executions.
More information: <https://manned.org/batch>.

- Execute commands from standard input (press `Ctrl + D` when done):

`batch`

- Execute a command from standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`

- Execute commands from a given file:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
