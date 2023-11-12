---
layout: page
title: linux/xdg-desktop-menu (English)
description: "Command-line tool for installing or uninstalling desktop menu items."
content_hash: 159d524d266b3f8799f1e286acd1512451eb9a18
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xdg-desktop-menu

Command-line tool for installing or uninstalling desktop menu items.
More information: <https://manned.org/xdg-desktop-menu>.

- Install an application to the desktop menu system:

`xdg-desktop-menu install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Install an application to the desktop menu system with the vendor prefix check disabled:

`xdg-desktop-menu install --novendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Uninstall an application from the desktop menu system:

`xdg-desktop-menu uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.desktop</span>

- Force an update of the desktop menu system:

`xdg-desktop-menu forceupdate --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|system</span>
