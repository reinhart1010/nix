---
layout: page
title: linux/emerge (English)
description: "Gentoo Linux package manager utility."
content_hash: c1dc844de733d4603445866fb956ce045317baa8
last_modified_at: 2022-12-05
---
# emerge

Gentoo Linux package manager utility.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Synchronize all packages:

`emerge --sync`

- Update all packages, including dependencies:

`emerge -uDNav @world`

- Resume a failed updated, skipping the failing package:

`emerge --resume --skipfirst`

- Install a new package, with confirmation:

`emerge -av `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package, with confirmation:

`emerge -Cav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove orphaned packages (that were installed only as dependencies):

`emerge -avc`

- Search the package database for a keyword:

`emerge -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
