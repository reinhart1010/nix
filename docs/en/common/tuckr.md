---
layout: page
title: common/tuckr (English)
description: "Dotfile manager written in Rust."
content_hash: 72ba1c86151adbb306eb1a9707cbb296ca908317
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# tuckr

Dotfile manager written in Rust.
See also: `chezmoi`, `vcsh`, `homeshick`, `stow`.
More information: <https://github.com/RaphGL/Tuckr>.

- Check dotfile status:

`tuckr status`

- Add all dotfiles to system:

`tuckr add \*`

- Add all dotfiles except specified programs:

`tuckr add \* -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program2</span>

- Remove all dotfiles from the system:

`tuckr rm \*`

- Add a program dotfile and run its setup script:

`tuckr set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
