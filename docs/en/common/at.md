---
layout: page
title: common/at (English)
description: "Execute commands once at a later time."
content_hash: b1e026616f9935794214916a34b19bec8a7aea08
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Execute commands once at a later time.
Service atd (or atrun) should be running for the actual executions.
More information: <https://manned.org/at>.

- Execute commands from `stdin` in 5 minutes (press `Ctrl + D` when done):

`at now + 5 minutes`

- Execute a command from `stdin` at 10:00 AM today:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- Execute commands from a given file next Tuesday:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 9:30 PM Tue`
