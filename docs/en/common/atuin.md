---
layout: page
title: common/atuin (English)
description: "Store your shell history in a searchable database."
content_hash: 73f510dc2b2d3e6d3736739abb3ae943e265cb10
last_modified_at: 2024-02-09
related_topics:
  - title: français version
    url: /fr/common/atuin.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atuin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atuin

Store your shell history in a searchable database.
Optionally sync your encrypted history between machines.
More information: <https://atuin.sh/docs/commands>.

- Install atuin into your shell:

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- Import history from the shell default history file:

`atuin import auto`

- Search shell history for a specific command:

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Register an account on the default sync server using the specified [u]sername, [e]mail and [p]assword:

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Login to the default sync server:

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Sync history with the sync server:

`atuin sync`
