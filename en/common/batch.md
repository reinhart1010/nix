---
layout: page
title: common/batch (English)
description: "Execute commands at a later time when the system load levels permit."
content_hash: 48cb74a5a27af72bf8452cf0c148c4fcdc84e475
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
More information: <https://man.archlinux.org/man/at.1>.

- Execute commands from standard input (press `Ctrl + D` when done):

`batch`

- Execute a command from standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`

- Execute commands from a given file:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
