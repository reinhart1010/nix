---
layout: page
title: common/atuin (English)
description: "Store your shell history in a searchable database."
content_hash: ddb03e98a5fd990e5fe9e454df1ca33faea12bd8
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># atuin

Store your shell history in a searchable database.
Optionally sync your encrypted history between machines.
More information: <https://atuin.sh/docs/overview/introduction/>.

- Install atuin into your shell:

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- Import history from the shell default history file:

`atuin import auto`

- Search shell history for a specific command:

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Register an account on the default sync server:

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Login to the default sync server:

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Sync history with the sync server:

`atuin sync`
