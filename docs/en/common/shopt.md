---
layout: page
title: common/shopt (English)
description: "Manage Bash shell options: variables (stored in `$BASHOPTS`) that control behavior specific to the Bash shell."
content_hash: fda760f03cf265cdaafa1341efa95724345d87f4
last_modified_at: 2023-12-27
tldri18n_status: 2
---
# shopt

Manage Bash shell options: variables (stored in `$BASHOPTS`) that control behavior specific to the Bash shell.
Generic POSIX shell variables (stored in `$SHELLOPTS`) are managed with the `set` command instead.
More information: <https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>.

- List of all settable options and whether they are set:

`shopt`

- Set an option:

`shopt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_name</span>

- Unset an option:

`shopt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_name</span>

- Print a list of all options and their status formatted as runnable `shopt` commands:

`shopt -p`

- Display help for the command:

`help shopt`
