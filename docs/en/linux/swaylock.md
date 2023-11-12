---
layout: page
title: linux/swaylock (English)
description: "Screen locking utility for Wayland compositors."
content_hash: 0b59f95fd14d12dad787df46a5af4942a4baed5a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# swaylock

Screen locking utility for Wayland compositors.
More information: <https://manned.org/swaylock>.

- Lock the screen showing a white background:

`swaylock`

- Lock the screen with a simple color background (rrggbb format):

`swaylock --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- Lock the screen to a PNG background:

`swaylock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Lock the screen and disable the unlock indicator (removes feedback on keypress):

`swaylock --no-unlock-indicator`

- Lock the screen and don't hide the mouse pointer:

`swaylock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Lock the screen to a PNG background tiled over all monitors:

`swaylock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>` --tiling`

- Lock the screen and show the number of failed login attempts:

`swaylock --show-failed-attempts`

- Load configuration from a file:

`swaylock --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config</span>
