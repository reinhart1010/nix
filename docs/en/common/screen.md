---
layout: page
title: common/screen (English)
description: "Hold a session open on a remote server. Manage multiple windows with a single SSH connection."
content_hash: e199ee1739c9e032e9c6e0f402b3861d8c1bb6fa
last_modified_at: 2023-12-29
tldri18n_status: 2
---
# screen

Hold a session open on a remote server. Manage multiple windows with a single SSH connection.
See also `tmux` and `zellij`.
More information: <https://manned.org/screen>.

- Start a new screen session:

`screen`

- Start a new named screen session:

`screen -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>

- Start a new daemon and log the output to `screenlog.x`:

`screen -dmLS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Show open screen sessions:

`screen -ls`

- Reattach to an open screen:

`screen -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>

- Detach from inside a screen:

`<Ctrl> + A, D`

- Kill the current screen session:

`<Ctrl> + A, K`

- Kill a detached screen:

`screen -X -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>` quit`
