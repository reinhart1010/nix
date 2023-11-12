---
layout: page
title: common/killall (English)
description: "Send kill signal to all instances of a process by name (must be exact name)."
content_hash: 435f4171f5c2a503a1b38c1f538a417d59f2c592
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# killall

Send kill signal to all instances of a process by name (must be exact name).
All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit.
More information: <https://manned.org/killall>.

- Terminate a process using the default SIGTERM (terminate) signal:

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- [l]ist available signal names (to be used without the 'SIG' prefix):

`killall -l`

- Interactively ask for confirmation before termination:

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Terminate a process using the SIGINT (interrupt) signal, which is the same signal sent by pressing `Ctrl + C`:

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Force kill a process:

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
