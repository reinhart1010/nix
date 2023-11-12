---
layout: page
title: common/phpbu (English)
description: "A backup utility framework for PHP."
content_hash: 084d44ab37e95bb06482478883e1af5b906b3b67
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/phpbu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpbu

A backup utility framework for PHP.
More information: <https://phpbu.de>.

- Run backups using the default `phpbu.xml` configuration file:

`phpbu`

- Run backups using a specific configuration file:

`phpbu --configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file.xml</span>

- Only run the specified backups:

`phpbu --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_task_name</span>

- Simulate the actions that would have been performed:

`phpbu --simulate`
