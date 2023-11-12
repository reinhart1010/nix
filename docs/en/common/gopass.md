---
layout: page
title: common/gopass (English)
description: "Standard Unix Password Manager for Teams. Written in Go."
content_hash: 15620eb63b57a195ef01893edf6df93dbc3b3246
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gopass

Standard Unix Password Manager for Teams. Written in Go.
More information: <https://www.gopass.pw>.

- Initialize the configuration settings:

`gopass init`

- Create a new entry:

`gopass new`

- Show all stores:

`gopass mounts`

- Mount a shared Git store:

`gopass mounts add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_repo_url</span>

- Search interactively using a keyword:

`gopass show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search using a keyword:

`gopass find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Sync all mounted stores:

`gopass sync`

- Show a particular password entry:

`gopass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">store_name|path/to/directory|email@email.com</span>
