---
layout: page
title: common/batch (English)
description: "Execute commands at a later time when the system load levels permit."
content_hash: fb49528253d59963c199192731f0984795c9fb45
last_modified_at: 2024-02-19
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
tldri18n_status: 2
---
# batch

Execute commands at a later time when the system load levels permit.
Service atd (or atrun) should be running for the actual executions.
More information: <https://manned.org/batch>.

- Execute commands from `stdin` (press `Ctrl + D` when done):

`batch`

- Execute a command from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`

- Execute commands from a given [f]ile:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
