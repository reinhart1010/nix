---
layout: page
title: linux/chrt (English)
description: "Manipulate the real-time attributes of a process."
content_hash: f0fbe37de2785f6cf33845834fe803e0e967052a
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

- Set the scheduling policy for a process:

`chrt --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deadline|idle|batch|rr|fifo|other</span>
