---
layout: page
title: linux/hyprctl (English)
description: "Control parts of the Hyprland Wayland compositor."
content_hash: 97f13722454ff59db4a06eb7c4ecac018bf6bfcd
last_modified_at: 2024-11-23
related_topics:
  - title: español version
    url: /es/linux/hyprctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/hyprctl.html
    icon: bi bi-globe
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

- Call a dispatcher:

`hyprctl dispatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispatcher</span>

- Set a configuration keyword dynamically:

`hyprctl keyword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Display version:

`hyprctl version`
