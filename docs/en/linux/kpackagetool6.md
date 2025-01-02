---
layout: page
title: linux/kpackagetool6 (English)
description: "KPackage Manager: install, list, remove Plasma packages."
content_hash: 920a49ea6dd25b127b4f84683c7105af8707315b
last_modified_at: 2025-01-02
tldri18n_status: 2
---
# kpackagetool6

KPackage Manager: install, list, remove Plasma packages.
More information: <https://manned.org/kpackagetool6>.

- List all known package types that can be installed:

`kpackagetool6 --list-types`

- Install the package from a directory:

`kpackagetool6 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Update installed package from a directory:

`kpackagetool6 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List installed plasmoids (`--global` for all users):

`kpackagetool6 --type Plasma/Applet --list --global`

- Remove a plasmoid by name:

`kpackagetool6 --type Plasma/Applet --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`
