---
layout: page
title: linux/i3lock (English)
description: "Simple screen locker built for the i3 window manager."
content_hash: 64ff022523868004a1b89855f1d9a815db5e14c9
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/i3lock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# i3lock

Simple screen locker built for the i3 window manager.
More information: <https://i3wm.org/i3lock>.

- Lock the screen showing a white background:

`i3lock`

- Lock the screen with a simple color background (rrggbb format):

`i3lock --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- Lock the screen to a PNG background:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Lock the screen and disable the unlock indicator (removes feedback on keypress):

`i3lock --no-unlock-indicator`

- Lock the screen and don't hide the mouse pointer:

`i3lock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Lock the screen to a PNG background tiled over all monitors:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>` --tiling`

- Lock the screen and show the number of failed login attempts:

`i3lock --show-failed-attempts`
