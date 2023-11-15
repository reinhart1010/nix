---
layout: page
title: linux/startx (English)
description: "A front-end to `xinit` that provides a nice user interface for running a single session of the X Window System."
content_hash: 574649cb5f8c7033045158762f8b611e3ad5a362
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# startx

A front-end to `xinit` that provides a nice user interface for running a single session of the X Window System.
More information: <https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- Start an X session:

`startx`

- Start an X session with a predefined depth value:

`startx -- -depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Start an X session with a predefined dpi value:

`startx -- -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Override the settings in the `.xinitrc` file and start a new X session:

`startx /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/window_manager_or_desktop_environment</span>
