---
layout: page
title: linux/chrt (English)
description: "Manipulate the real-time attributes of a process."
content_hash: 731e93761837df58293ed0c1e3f5329c279882ba
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# chrt

Manipulate the real-time attributes of a process.
More information: <https://manned.org/chrt>.

- Display attributes of a process:

`chrt --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Display attributes of all threads of a process:

`chrt --all-tasks --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Display the min/max priority values that can be used with `chrt`:

`chrt --max`

- Set the scheduling priority of a process:

`chrt --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Set the scheduling policy of a process:

`chrt --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deadline|idle|batch|rr|fifo|other</span>` --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
