---
layout: page
title: common/gopass (English)
description: "Standard Unix Password Manager for Teams. Written in Go."
content_hash: 98e26c45050d1189aad8924e836c0ab7641b669e
---
# gopass

Standard Unix Password Manager for Teams. Written in Go.
More information: <https://www.gopass.pw>.

- Initialise the configuration settings:

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
