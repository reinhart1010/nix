---
layout: page
title: linux/killall (English)
description: "Send kill signal to all instances of a process by name (must be exact name)."
content_hash: 266063638307b01c040bb294c72c16fba90c4a5d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# killall

Send kill signal to all instances of a process by name (must be exact name).
All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit.
More information: <https://manned.org/killall>.

- Terminate a process using the default SIGTERM (terminate) signal:

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- List available signal names (to be used without the 'SIG' prefix):

`killall --list`

- Interactively ask for confirmation before termination:

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Terminate a process using the SIGINT (interrupt) signal, which is the same signal sent by pressing `Ctrl + C`:

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Force kill a process:

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
