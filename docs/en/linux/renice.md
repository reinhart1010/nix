---
layout: page
title: linux/renice (English)
description: "Alter the scheduling priority/niceness of running processes."
content_hash: 140e34a28f7c7fbe3c47698a3957bca4f0fb5e97
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# renice

Alter the scheduling priority/niceness of running processes.
Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
See also: `nice`.
More information: <https://manned.org/renice>.

- Set the absolute priority of a running [p]rocess:

`renice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Increase/decrease the priority of all processes owned by a [u]ser:

`renice --relative `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|user</span>

- Set the priority of all processes that belong to a process [g]roup:

`renice --absolute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_group</span>
