---
layout: page
title: linux/wmctrl (English)
description: "CLI for X Window Manager."
content_hash: 21744e928c2d30490b2624fa59e3a5dcab9d6c24
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wmctrl

CLI for X Window Manager.
More information: <https://manned.org/wmctrl>.

- List all windows, managed by the window manager:

`wmctrl -l`

- Switch to the first window whose (partial) title matches:

`wmctrl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_title</span>

- Move a window to the current workspace, raise it and give it focus:

`wmctrl -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_title</span>

- Switch to a workspace:

`wmctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_number</span>

- Select a window and toggle fullscreen:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_title</span>` -b toggle,fullscreen`

- Select a window a move it to a workspace:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_title</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_number</span>
