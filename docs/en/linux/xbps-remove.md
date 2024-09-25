---
layout: page
title: linux/xbps-remove (English)
description: "XBPS utility to remove packages."
content_hash: 36c60a024c2c4c81e5778db2a0f02b23e2bd28c0
last_modified_at: 2024-09-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/xbps-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-remove

XBPS utility to remove packages.
See also: `xbps`.
More information: <https://manned.org/xbps-remove.1>.

- Remove a package:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove orphan packages (installed as dependencies but no longer required by any package):

`xbps-remove --remove-orphans`

- Remove obsolete packages from the cache:

`xbps-remove --clean-cache`
