---
layout: page
title: common/set (English)
description: "Toggle shell options or set the values of positional parameters."
content_hash: 6cbb2670baa863ec2ebf5dbef19bcdd9e4245090
last_modified_at: 2024-12-21
related_topics:
  - title: 한국어 version
    url: /ko/common/set.html
    icon: bi bi-globe
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

- Return to default mode:

`set -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>

- List all modes:

`set -o`

- Exit the shell when (some) commands fail:

`set -e`

- Reset all shell parameters and assign new ones:

`set -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2...</span>
