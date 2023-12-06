---
layout: page
title: common/xteddy (English)
description: "A cuddly teddy bear for your X Windows desktop."
content_hash: c150e13e69dbcf0d580097fa53b8c620d661421b
last_modified_at: 2023-12-06
tldri18n_status: 2
---
# xteddy

A cuddly teddy bear for your X Windows desktop.
More information: <https://manned.org/xteddy.1>.

- Display a cuddly teddy bear on your X desktop:

`xteddy`

- Use the window manager to display the teddy bear and ignore the "quit" (`q`) command:

`xteddy -wm -noquit`

- Make the teddy bear stay on top of all other windows:

`xteddy -float`

- Display another image [F]ile instead of the cuddly teddy bear:

`xteddy -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Set the initial location of the teddy bear (`width` and `height` are ignored):

`xteddy -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>
