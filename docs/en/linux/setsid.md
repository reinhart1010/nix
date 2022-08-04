---
layout: page
title: linux/setsid (English)
description: "Run a program in a new session if the calling process is not a process group leader."
content_hash: 6906fd36ee686ef5a41c670a09e2880a1e535ee2
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># setsid

Run a program in a new session if the calling process is not a process group leader.
The created session is by default not controlled by the current terminal.
More information: <https://manned.org/setsid>.

- Run a program in a new session:

`setsid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Run a program in a new session discarding the resulting output and error:

`setsid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>` > /dev/null 2>&1`

- Run a program creating a new process:

`setsid --fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Return the exit code of a program as the exit code of setsid when the program exits:

`setsid --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Run a program in a new session setting the current terminal as the controlling terminal:

`setsid --ctty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
