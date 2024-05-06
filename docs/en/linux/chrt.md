---
layout: page
title: linux/chrt (English)
description: "Manipulate the real-time attributes of a process."
content_hash: bc373d15a2697f95b0d164f4cf596118e28290bc
last_modified_at: 2024-05-06
tldri18n_status: 2
---
# chrt

Manipulate the real-time attributes of a process.
More information: <https://man7.org/linux/man-pages/man1/chrt.1.html>.

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
