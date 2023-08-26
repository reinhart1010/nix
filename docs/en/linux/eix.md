---
layout: page
title: linux/eix (English)
description: "Utilities for searching local Gentoo packages."
content_hash: a3ed4e13ef5f68febd4319af4a14dc181b7e6721
last_modified_at: 2023-08-26
---
# eix

Utilities for searching local Gentoo packages.
Update local package cache using `eix-update`.
More information: <https://wiki.gentoo.org/wiki/Eix>.

- Search for a package:

`eix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Search for installed packages:

`eix --installed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Search in package descriptions:

`eix --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">description</span>`"`

- Search by package license:

`eix --license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license</span>

- Exclude results from search:

`eix --not --license `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">license</span>
