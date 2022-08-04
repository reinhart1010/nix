---
layout: page
title: linux/bspc (English)
description: "A tool to control `bspwm`."
content_hash: 7c4524719502c211207129017fb26b3094d0558f
---
# bspc

A tool to control `bspwm`.
More information: <https://github.com/baskerville/bspwm>.

- Define two virtual desktop:

`bspc monitor --reset-desktops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Focus the given desktop:

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Close the windows rooted at the selected node:

`bspc node --close`

- Send the selected node to the given desktop:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Toggle full screen mode for the selected node:

`bspc node --state ~fullscreen`
