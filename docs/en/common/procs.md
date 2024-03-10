---
layout: page
title: common/procs (English)
description: "Display information about the active processes."
content_hash: 07a7d7c63e6165ae3720d5bf3018ebac255273ac
last_modified_at: 2024-03-10
tldri18n_status: 2
---
# procs

Display information about the active processes.
More information: <https://github.com/dalance/procs>.

- List all processes showing the PID, user, CPU usage, memory usage, and the command which started them:

`procs`

- List all processes as a tree:

`procs --tree`

- List information about processes, if the commands which started them contain Zsh:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>

- List information about all processes sorted by CPU time in [a]scending or [d]escending order:

`procs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--sorta|--sortd</span>` cpu`

- List information about processes with either a PID, command, or user containing `41` or `firefox`:

`procs --or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID|command|user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- List information about processes with both PID `41` and a command or user containing `zsh`:

`procs --and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">41</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
