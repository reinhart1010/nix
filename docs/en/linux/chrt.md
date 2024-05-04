---
layout: page
title: linux/chrt (English)
description: "Manipulate the real-time attributes of a process."
content_hash: 8090363d3025f86f21e2c7386e71366d93436209
last_modified_at: 2024-05-04
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

- Set the scheduling policy for a process:

`chrt --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deadline|idle|batch|rr|fifo|other</span>` --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
