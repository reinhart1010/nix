---
layout: page
title: linux/setxkbmap (English)
description: "Set the keyboard using the X Keyboard Extension."
content_hash: e9498508896b674f5bda9ce9ef3ab6887e665cb9
---
# setxkbmap

Set the keyboard using the X Keyboard Extension.

- Set the keyboard in French AZERTY:

`setxkbmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fr</span>

- Set multiple keyboard layouts, their variants and switching option:

`setxkbmap -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us,de</span>` -variant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,qwerty</span>` -option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'grp:alt_caps_toggle'</span>

- Get help:

`setxkbmap -help`

- List all layouts:

`localectl list-x11-keymap-layouts`

- List variants for the layout:

`localectl list-x11-keymap-variants `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>

- List available switching options:

`localectl list-x11-keymap-options | grep grp:`
