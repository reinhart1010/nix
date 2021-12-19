---
layout: page
title: linux/spi (English)
description: "A meta package manager that handles both packages and slackbuilds."
content_hash: d5a3f27b49440d4b57682dda4bd6587e47e7f96b
---
# spi

A meta package manager that handles both packages and slackbuilds.
More information: <https://github.com/gapan/spi>.

- Update the list of available packages and slackbuilds:

`spi --update`

- Install a package or slackbuild:

`spi --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package/slackbuild_name</span>

- Upgrade all installed packages to the latest versions available:

`spi --upgrade`

- Locate packages or slackbuilds by package name or description:

`spi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_terms</span>

- Display information about a package or slackbuild:

`spi --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package/slackbuild_name</span>

- Purge the local package and slackbuild caches:

`spi --clean`
