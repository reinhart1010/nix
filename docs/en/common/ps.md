---
layout: page
title: common/ps (English)
description: "Information about running processes."
content_hash: e4411259fee0575731faea1e672aa15ffc02a859
last_modified_at: 2024-04-25
related_topics:
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

Information about running processes.
More information: <https://manned.org/ps>.

- List all running processes:

`ps aux`

- List all running processes including the full command string:

`ps auxww`

- Search for a process that matches a string (the brackets will prevent `grep` from matching itself):

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[s]tring</span>

- List all processes of the current user in extra full format:

`ps --user $(id -u) -F`

- List all processes of the current user as a tree:

`ps --user $(id -u) f`

- Get the parent PID of a process:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Sort processes by memory consumption:

`ps --sort size`
