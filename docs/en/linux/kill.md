---
layout: page
title: linux/kill (English)
description: "Sends a signal to a process, usually related to stopping the process."
content_hash: 064e75a9b73fdbf7ad07047dedecddde6ca5828c
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/kill.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Sends a signal to a process, usually related to stopping the process.
All signals except for SIGKILL and SIGSTOP can be intercepted by the process to perform a clean exit.
More information: <https://manned.org/kill>.

- Terminate a program using the default SIGTERM (terminate) signal:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- List signal values and their corresponding names (to be used without the `SIG` prefix). The available options may depend on the `kill` implementation:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|-L|--table</span>

- Terminate a background job:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Terminate a program using the SIGINT (interrupt) signal. This is typically initiated by the user pressing `Ctrl + C`:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Signal the operating system to pause a program until a SIGCONT ("continue") signal is received:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_id</span>

- Send a `SIGUSR1` signal to all processes with the given GID (group id):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>
