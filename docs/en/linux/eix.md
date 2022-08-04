---
layout: page
title: linux/eix (English)
description: "Utilities for searching local Gentoo packages."
content_hash: ac44c4012357e8f3aa2ad64c4eab731b1d872723
---
# eix

Utilities for searching local Gentoo packages.
Update local package cache using `eix-update`.
More information: <https://wiki.gentoo.org/wiki/Eix>.

- Search for a package:

`eix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search for installed packages:

`eix --installed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search in package descriptions:

`eix --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Search by package license:

`eix --license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license</span>

- Exclude results from search:

`eix --not --license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license</span>
