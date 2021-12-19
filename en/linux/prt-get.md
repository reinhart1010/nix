---
layout: page
title: linux/prt-get (English)
description: "The CRUX package manager."
content_hash: 4cd478c9faa9f388ab1612e6cc83fff4342977e1
---
# prt-get

The CRUX package manager.

- Install a package:

`prt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install a package with dependency handling:

`prt-get depinst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Update a package manually:

`prt-get upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package:

`prt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Upgrade the system from the local ports tree:

`prt-get sysup`

- Search the ports tree:

`prt-get search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Search for a file in a package:

`prt-get fsearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
