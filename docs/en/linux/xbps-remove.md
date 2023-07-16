---
layout: page
title: linux/xbps-remove (English)
description: "XBPS utility to remove packages."
content_hash: b2b0065c5ca63a830589abb45040f1ace57f249e
last_modified_at: 2023-07-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xbps-remove

XBPS utility to remove packages.
See also: `xbps`.
More information: <https://man.voidlinux.org/xbps-remove.1>.

- Remove a package:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove orphan packages (installed as dependencies but no longer required by any package):

`xbps-remove --remove-orphans`

- Remove obsolete packages from the cache:

`xbps-remove --clean-cache`
