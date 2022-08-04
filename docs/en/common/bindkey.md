---
layout: page
title: common/bindkey (English)
description: "Add keybindings to Z-Shell."
content_hash: d60f75fabb94c611f1f311252ac9b42c2ede92d0
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bindkey

Add keybindings to Z-Shell.
More information: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- Bind a hotkey to a specific command:

`bindkey "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^k</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kill-line</span>

- Bind a hotkey to a specific key sequence:

`bindkey -s '^o' 'cd ..\n'`

- View keymaps:

`bindkey -l`

- View the hotkey in a keymap:

`bindkey -M main`
