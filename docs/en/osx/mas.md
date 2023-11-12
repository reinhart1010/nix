---
layout: page
title: osx/mas (English)
description: "Command-line interface for the Mac App Store."
content_hash: 16f04ca0ae727890097118c83fc261941181f09f
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/mas.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mas

Command-line interface for the Mac App Store.
More information: <https://github.com/mas-cli/mas>.

- Sign into the Mac App Store for the first time:

`mas signin "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>`"`

- Show all installed applications and their product identifiers:

`mas list`

- Search for an application, displaying the price alongside the results:

`mas search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>`" --price`

- Install or update an application:

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_identifier</span>

- Install all pending updates:

`mas upgrade`
