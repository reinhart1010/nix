---
layout: page
title: linux/emerge (English)
description: "Gentoo Linux package manager utility."
content_hash: eee120cb9ce8cab358f9141bff6229fd7f9c9808
last_modified_at: 2024-11-30
related_topics:
  - title: 한국어 version
    url: /ko/linux/emerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emerge

Gentoo Linux package manager utility.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Synchronize all packages:

`sudo emerge --sync`

- Update all packages, including dependencies:

`sudo emerge -uDNav @world`

- Resume a failed updated, skipping the failing package:

`sudo emerge --resume --skipfirst`

- Install a new package, with confirmation:

`sudo emerge -av `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package, with confirmation:

`sudo emerge -Cav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove orphaned packages (that were installed only as dependencies):

`sudo emerge -avc`

- Search the package database for a keyword:

`emerge -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
