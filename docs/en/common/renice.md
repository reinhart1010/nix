---
layout: page
title: common/renice (English)
description: "Alters the scheduling priority/niceness of one or more running processes."
content_hash: 9e14f1705af4240bb3f8f0c47d5761bb2a341201
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/renice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# renice

Alters the scheduling priority/niceness of one or more running processes.
Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
More information: <https://manned.org/renice>.

- Change priority of a running process:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Change priority of all processes owned by a user:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Change priority of all processes that belong to a process group:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` --pgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_group</span>
