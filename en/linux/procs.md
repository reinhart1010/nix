---
layout: page
title: linux/procs (English)
description: "Display information about the active processes."
content_hash: cb25220b6200529bf8a31baa4ea38aed7aa89189
---
# procs

Display information about the active processes.
More information: <https://github.com/dalance/procs>.

- List all processes showing the PID, user, CPU usage, memory usage, and the command which started them:

`procs`

- Show information about processes, if the commands which started them contain `zsh`:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>

- Show information about all processes sorted by CPU time in [a]scending or [d]escending order:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--sortd|--sorta</span>` cpu`

- Show information about processes with either a PID, command, or user containing (`zsh` or `firefox`):

`procs --or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID|command|user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Show information about processes with both PID `41` and a command or user containing `zsh`:

`procs --and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
