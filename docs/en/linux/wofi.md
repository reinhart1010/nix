---
layout: page
title: linux/wofi (English)
description: "An application launcher for wlroots-based Wayland compositors, similar to `rofi` and `dmenu`."
content_hash: 56d9d0bcda8d33ce0438f811d01c337a08bcc855
last_modified_at: 2024-09-07
tldri18n_status: 2
---
# wofi

An application launcher for wlroots-based Wayland compositors, similar to `rofi` and `dmenu`.
More information: <https://hg.sr.ht/~scoopta/wofi>.

- Show the list of apps:

`wofi --show drun`

- Show the list of all commands:

`wofi --show run`

- Pipe a list of items to `stdin` and print the selected item to `stdout`:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Choice1\nChoice2\nChoice3</span>`" | wofi --dmenu`
