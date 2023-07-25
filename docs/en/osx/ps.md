---
layout: page
title: osx/ps (English)
description: "Information about running processes."
content_hash: ccee8efb8e8d337adb26aa2ca44adec8053c2c23
last_modified_at: 2023-07-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ps

Information about running processes.
More information: <https://www.unix.com/man-page/osx/1/ps/>.

- List all running processes:

`ps aux`

- List all running processes including the full command string:

`ps auxww`

- Search for a process that matches a string:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Get the parent PID of a process:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sort processes by memory usage:

`ps -m`

- Sort processes by CPU usage:

`ps -r`
