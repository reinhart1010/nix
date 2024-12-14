---
layout: page
title: common/batch (English)
description: "Execute commands at a later time when the system load levels permit."
content_hash: da4dfddbbadbdbc3de8d8bbe0ce96f9f7e8b5a9d
last_modified_at: 2024-12-14
related_topics:
  - title: español version
    url: /es/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# batch

Execute commands at a later time when the system load levels permit.
Results will be sent to the user's mail.
See also: `at`, `atq`, `atrm` `mail`.
More information: <https://manned.org/batch>.

- Start the `atd` daemon:

`systemctl start atd`

- Execute commands from `stdin` (press `Ctrl + D` when done):

`batch`

- Execute a command from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`
