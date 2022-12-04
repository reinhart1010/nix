---
layout: page
title: linux/rofi (English)
description: "An application launcher and window switcher."
content_hash: 22d8565affc30c00e68f049341b9deece61de729
last_modified_at: 2022-12-04
---
# rofi

An application launcher and window switcher.
More information: <https://github.com/davatorium/rofi>.

- Show the list of apps:

`rofi -show drun`

- Show the list of all commands:

`rofi -show run`

- Switch between windows:

`rofi -show window`

- Pipe a list of items to `stdin` and print the selected item to `stdout`:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Choice1\nChoice2\nChoice3</span>`" | rofi -dmenu`
