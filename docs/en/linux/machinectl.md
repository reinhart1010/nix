---
layout: page
title: linux/machinectl (English)
description: "Control the systemd machine manager."
content_hash: eb4939c472a42495a81c945d845371a2f33eab9e
last_modified_at: 2023-10-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># machinectl

Control the systemd machine manager.
Execute operations on virtual machines, containers and images.
More information: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- Start a machine as a service using `systemd-nspawn`:

`sudo machinectl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine_name</span>

- Stop a running machine:

`sudo machinectl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine_name</span>

- Display a list of running machines:

`machinectl list`

- Open an interactive shell inside the machine:

`sudo machinectl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">machine_name</span>
