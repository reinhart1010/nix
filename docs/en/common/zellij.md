---
layout: page
title: common/zellij (English)
description: "Terminal multiplexer with batteries included."
content_hash: 7b79ba49e305ed9325a115819f382dae306fb7d7
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# zellij

Terminal multiplexer with batteries included.
See also `tmux` and `screen`.
More information: <https://zellij.dev/documentation/>.

- Start a new named session:

`zellij --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List existing sessions:

`zellij list-sessions`

- Attach to the most recently used session:

`zellij attach`

- Open a new pane (inside a zellij session):

`<Alt> + N`

- Detach from the current session (inside a zellij session):

`<Ctrl> + O, D`
