---
layout: page
title: linux/kpackagetool5 (English)
description: "KPackage Manager: Install, list, remove Plasma packages."
content_hash: 4d68fd4161d6e1eb4db33d31650739ff3f41aa30
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kpackagetool5

KPackage Manager: Install, list, remove Plasma packages.
More information: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>.

- List all known package types that can be installed:

`kpackagetool5 --list-types`

- Install the package from a directory:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Update installed package from a directory:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List installed plasmoids (--global for all users):

`kpackagetool5 --type Plasma/Applet --list --global`

- Remove a plasmoid by name:

`kpackagetool5 --type Plasma/Applet --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`
