---
layout: page
title: linux/debtap (English)
description: "Convert Debian packages into Arch Linux packages."
content_hash: 2f2ac3da83845dc5d02d98cae3da06f228d08f49
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# debtap

Convert Debian packages into Arch Linux packages.
See also: `pacman-upgrade`.
More information: <https://github.com/helixarch/debtap>.

- Update debtap database (before the first run):

`sudo debtap --update`

- Convert the specified package:

`debtap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>

- Convert the specified package bypassing all questions, except for editing metadata files:

`debtap --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>

- Generate a PKGBUILD file:

`debtap --pkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.deb</span>
