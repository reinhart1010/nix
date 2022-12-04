---
layout: page
title: common/gibo (English)
description: "Fetch gitignore boilerplates."
content_hash: b0613636affb0e53d704b80fc653855ee08ad9cf
last_modified_at: 2022-12-04
---
# gibo

Fetch gitignore boilerplates.
More information: <https://github.com/simonwhitaker/gibo>.

- List available boilerplates:

`gibo list`

- Write a boilerplate to `stdout`:

`gibo dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">boilerplate</span>

- Write a boilerplate to .gitignore:

`gibo dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">boilerplate</span>` >>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.gitignore</span>

- Search for boilerplates containing a given string:

`gibo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Update available local boilerplates:

`gibo update`
