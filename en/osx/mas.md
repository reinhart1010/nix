---
layout: page
title: osx/mas (English)
description: "Command-line interface for the Mac App Store."
content_hash: 60d68f2be968065c23b67cd6aa0ca290e3c3107b
related_topics:
  - title: 中文 version
    url: /zh/osx/mas.html
    icon: bi bi-globe
---
# mas

Command-line interface for the Mac App Store.
More information: <https://github.com/mas-cli/mas>.

- Sign into the Mac App Store for the first time:

`mas signin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- Show all installed applications and their product identifiers:

`mas list`

- Search for an application, displaying the price alongside the results:

`mas search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application</span>` --price`

- Install or update an application:

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_identifier</span>

- Install all pending updates:

`mas upgrade`
