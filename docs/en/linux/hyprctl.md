---
layout: page
title: linux/hyprctl (English)
description: "Control parts of the Hyprland Wayland compositor."
content_hash: fdb29f14485dd4a700bc5c377135000b8c77f881
last_modified_at: 2024-06-15
tldri18n_status: 2
---
# hyprctl

Control parts of the Hyprland Wayland compositor.
More information: <https://wiki.hyprland.org/Configuring/Using-hyprctl>.

- Reload Hyprland configuration:

`hyprctl reload`

- Return the active window name:

`hyprctl activewindow`

- List all connected input devices:

`hyprctl devices`

- List all outputs with respective properties:

`hyprctl workspaces`

- Call a dispatcher with an argument:

`hyprctl dispatch exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>

- Set a configuration keyword dynamically:

`hyprctl keyword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Display version:

`hyprctl version`
