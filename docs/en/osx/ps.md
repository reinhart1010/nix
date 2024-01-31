---
layout: page
title: osx/ps (English)
description: "Information about running processes."
content_hash: ea1e4bb2d027e5c3c7efa2d462609e25bea61224
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Information about running processes.
More information: <https://keith.github.io/xcode-man-pages/ps.1.html>.

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
