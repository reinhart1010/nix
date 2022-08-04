---
layout: page
title: linux/cpulimit (English)
description: "A tool to throttle the CPU usage of other processes."
content_hash: 59c1a39802e63b5b7e5498d4a7c923141d9166f7
related_topics:
  - title: español version
    url: /es/linux/cpulimit.html
    icon: bi bi-globe
---
# cpulimit

A tool to throttle the CPU usage of other processes.
More information: <http://cpulimit.sourceforge.net/>.

- Limit an existing process with PID 1234 to only use 25% of the CPU:

`cpulimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25%</span>

- Limit an existing program by its executable name:

`cpulimit --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Launch a given program and limit it to only use 50% of the CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program arg1 arg2 ...</span>

- Launch a program, limit its CPU usage to 50% and run cpulimit in the background:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --background -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Kill its process if the program's CPU usage goes over 50%:

`cpulimit --limit 50 --kill -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Throttle both it and its child processes so that none go about 25% CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` --monitor-forks -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
