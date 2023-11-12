---
layout: page
title: common/tuckr (English)
description: "Dotfile manager written in Rust."
content_hash: 79b46a7cabf73e3ffc50857759cf507005847174
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tuckr

Dotfile manager written in Rust.
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
