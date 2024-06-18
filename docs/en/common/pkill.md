---
layout: page
title: common/pkill (English)
description: "Signal process by name."
content_hash: 695378962304644cd343a35900b5ccda2142e1d4
last_modified_at: 2024-06-18
related_topics:
  - title: 한국어 version
    url: /ko/common/pkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkill

Signal process by name.
Mostly used for stopping processes.
More information: <https://www.manned.org/pkill>.

- Kill all processes which match:

`pkill "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`

- Kill all processes which match their full command instead of just the process name:

`pkill -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>`"`

- Force kill matching processes (can't be blocked):

`pkill -9 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`

- Send SIGUSR1 signal to processes which match:

`pkill -USR1 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`

- Kill the main `firefox` process to close the browser:

`pkill --oldest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>`"`
