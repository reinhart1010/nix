---
layout: page
title: linux/repo-add (English)
description: "Package database maintenance utility which enables installation of said package via Pacman."
content_hash: 8e5df5d67ab3f4cca833003f241e9c01a39ac943
last_modified_at: 2024-02-24
tldri18n_status: 2
---
# repo-add

Package database maintenance utility which enables installation of said package via Pacman.
More information: <https://man.archlinux.org/man/repo-add>.

- Create an empty repository:

`repo-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>

- Add all package binaries in the current directory and remove the old database file:

`repo-add --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- Add all package binaries in the current directory without showing color:

`repo-add --nocolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>
