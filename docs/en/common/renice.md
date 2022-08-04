---
layout: page
title: common/renice (English)
description: "Alters the scheduling priority/nicenesses of one or more running processes."
content_hash: 2cc9cfd9ff8572c9586c47edcf53a0c727170fc3
---
# renice

Alters the scheduling priority/nicenesses of one or more running processes.
Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
More information: <https://manned.org/renice>.

- Change priority of a running process:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Change priority of all processes owned by a user:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Change priority of all processes that belong to a process group:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_value</span>` --pgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_group</span>
