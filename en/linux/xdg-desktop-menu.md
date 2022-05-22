---
layout: page
title: linux/xdg-desktop-menu (English)
description: "Command-line tool for installing or uninstalling desktop menu items."
content_hash: f42048a6e2b2201421a2f22f370d725803122da4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xdg-desktop-menu

Command-line tool for installing or uninstalling desktop menu items.
More information: <https://manned.org/xdg-desktop-menu>.

- Install an application to the desktop menu system:

`xdg-desktop-menu install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Install an application to the desktop menu system with the vendor prefix check disabled:

`xdg-desktop-menu install --novendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Uninstall an application from the desktop menu system:

`xdg-desktop-menu uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Force an update of the desktop menu system:

`xdg-desktop-menu --forceupdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|system</span>
