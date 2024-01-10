---
layout: page
title: linux/ionice (English)
description: "Get or set program I/O scheduling class and priority."
content_hash: 99b1cd46e218a5c8693ea3b2b5566a0afde177ba
last_modified_at: 2024-01-10
tldri18n_status: 2
---
# ionice

Get or set program I/O scheduling class and priority.
Scheduling classes: 1 (realtime), 2 (best-effort), 3 (idle).
Priority levels: 0 (the highest) - 7 (the lowest).
More information: <https://manned.org/ionice>.

- Run a command with the given scheduling class and priority:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheduling_class</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Set I/O scheduling [c]lass of a running process with a specific [p]id, [P]gid or [u]id:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheduling_class</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">p|P|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Run a command with custom I/O scheduling [c]lass and priority:

`ionice -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheduling_class</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Ignore failure to set the requested priority:

`ionice -t -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Run the command even in case it was not possible to set the desired priority (this can happen due to insufficient privileges or an old kernel version):

`ionice -t -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Print the I/O scheduling class and priority of a running process:

`ionice -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
