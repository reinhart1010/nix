---
layout: page
title: linux/prlimit (English)
description: "Get or set process resource soft and hard limits."
content_hash: f5938b281596872dac8ed5c313c21a6da33b6426
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# prlimit

Get or set process resource soft and hard limits.
Given a process ID and one or more resources, prlimit tries to retrieve and/or modify the limits.
More information: <https://manned.org/prlimit>.

- Display limit values for all current resources for the running parent process:

`prlimit`

- Display limit values for all current resources of a specified process:

`prlimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid_number</span>

- Run a command with a custom number of open files limit:

`prlimit --nofile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
