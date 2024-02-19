---
layout: page
title: common/bindkey (English)
description: "Add keybindings to Z-Shell."
content_hash: f0ccf261bacfebf74493ad602ffe8fbd362b45e4
last_modified_at: 2024-02-19
tldri18n_status: 2
---
# bindkey

Add keybindings to Z-Shell.
More information: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- Bind a hotkey to a specific command:

`bindkey "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^k</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kill-line</span>

- Bind a hotkey to a specific key [s]equence:

`bindkey -s '^o' 'cd ..\n'`

- [l]ist keymaps:

`bindkey -l`

- View the hotkey in a key[M]ap:

`bindkey -M main`
