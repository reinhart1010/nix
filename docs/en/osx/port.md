---
layout: page
title: osx/port (English)
description: "Package manager for macOS."
content_hash: 701cc798927b7699b6b3fd6ff3014091e1030cbc
last_modified_at: 2023-08-26
related_topics:
  - title: español version
    url: /es/osx/port.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/port.html
    icon: bi bi-globe
---
# port

Package manager for macOS.
More information: <https://www.macports.org>.

- Search for a package:

`port search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Install a package:

`sudo port install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List installed packages:

`port installed`

- Update port and fetch the latest list of available packages:

`sudo port selfupdate`

- Upgrade outdated packages:

`sudo port upgrade outdated`

- Remove old versions of installed packages:

`sudo port uninstall inactive`
