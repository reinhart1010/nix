---
layout: page
title: common/twm (English)
description: "A window manager for the X Window system."
content_hash: 1ffc55eb2454961af348704d41eeb662d55d76d8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# twm

A window manager for the X Window system.
More information: <https://gitlab.freedesktop.org/xorg/app/twm>.

- Connect to the default X server:

`twm`

- Connect to a specific X server:

`twm -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">display</span>

- Only manage the default screen:

`twm -s`

- Use a specific startup file:

`twm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Enable verbose mode and print unexpected errors in X:

`twm -v`
