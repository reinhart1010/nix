---
layout: page
title: linux/prlimit (English)
description: "Get or set process resource soft and hard limits."
content_hash: ea7549b2401ade5fec27c812a6afdd686d05ecce
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prlimit

Get or set process resource soft and hard limits.
Given a process ID and one or more resources, prlimit tries to retrieve and/or modify the limits.
More information: <https://manned.org/prlimit>.

- Display limit values for all current resources for the running parent process:

`prlimit`

- Display limit values for all current resources of a specified process:

`prlimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid number</span>

- Run a command with a custom number of open files limit:

`prlimit --nofile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
