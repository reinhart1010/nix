---
layout: page
title: common/set (English)
description: "Toggle shell options or set the values of positional parameters."
content_hash: 88fd9f54b770b14dc77562944983e13ea8f3272d
last_modified_at: 2024-06-17
tldri18n_status: 2
---
# set

Toggle shell options or set the values of positional parameters.
More information: <https://manned.org/set.1posix>.

- Display the names and values of shell variables:

`set`

- Export newly initialized variables to child processes:

`set -a`

- Write formatted messages to `stderr` when jobs finish:

`set -b`

- Write and edit text in the command-line with `vi`-like keybindings (e.g. `yy`):

`set -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vi</span>

- Exit the shell when (some) commands fail:

`set -e`
