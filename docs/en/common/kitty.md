---
layout: page
title: common/kitty (English)
description: "A fast, feature-rich, GPU based terminal emulator."
content_hash: b26f670dee3d62d7b90e968b67f3cc65bc7da6cf
---
# kitty

A fast, feature-rich, GPU based terminal emulator.
More information: <https://sw.kovidgoyal.net/kitty/>.

- Open a new terminal:

`kitty`

- Open a terminal with the specified title for the window:

`kitty --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>`"`

- Start the theme-chooser builtin:

`kitty +kitten themes`

- Display an image in the terminal:

`kitty +kitten icat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image</span>

- Copy the contents of stdin to the clipboard:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example</span>` | kitty +kitten clipboard`
