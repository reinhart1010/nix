---
layout: page
title: linux/kpackagetool5 (English)
description: "KPackage Manager: install, list, remove Plasma packages."
content_hash: d5b55a42a6b6d068876c772f6ce5b0f2b4418078
last_modified_at: 2025-01-01
related_topics:
  - title: 한국어 version
    url: /ko/linux/kpackagetool5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kpackagetool5

KPackage Manager: install, list, remove Plasma packages.
More information: <https://manned.org/kpackagetool5>.

- List all known package types that can be installed:

`kpackagetool5 --list-types`

- Install the package from a directory:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Update installed package from a directory:

`kpackagetool5 --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_type</span>` --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- List installed plasmoids (`--global` for all users):

`kpackagetool5 --type Plasma/Applet --list --global`

- Remove a plasmoid by name:

`kpackagetool5 --type Plasma/Applet --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`
