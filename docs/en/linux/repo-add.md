---
layout: page
title: linux/repo-add (English)
description: "Package database maintenance utility which enables installation of said package via Pacman."
content_hash: ebb5c71dfbbf80f8c948bc7d5e73a3b38bd9c279
last_modified_at: 2024-09-25
tldri18n_status: 2
---
# repo-add

Package database maintenance utility which enables installation of said package via Pacman.
More information: <https://manned.org/repo-add>.

- Create an empty repository:

`repo-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>

- Add all package binaries in the current directory and remove the old database file:

`repo-add --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- Add all package binaries in the current directory without showing color:

`repo-add --nocolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>
