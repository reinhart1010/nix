---
layout: page
title: common/ionice (English)
description: "Get or set program I/O scheduling class and priority."
content_hash: e1b40d13c8263281c71796d5acf6d67e3b6f6374
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ionice

Get or set program I/O scheduling class and priority.
Scheduling classes: 1 (realtime), 2 (best-effort), 3 (idle).
Priority levels: 0 (the highest) - 7 (the lowest).
More information: <https://manned.org/ionice>.

- Set I/O scheduling class of a running process:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheduling_class</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Run a command with custom I/O scheduling class and priority:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheduling_class</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Print the I/O scheduling class and priority of a running process:

`ionice -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
