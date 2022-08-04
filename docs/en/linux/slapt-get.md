---
layout: page
title: linux/slapt-get (English)
description: "An apt like system for Slackware package management."
content_hash: f9c18f73c457c66f6000ea9a7f3923096d165646
---
# slapt-get

An apt like system for Slackware package management.
Package sources need to be configured in the slapt-getrc file.
More information: <https://software.jaos.org>.

- Update the list of available packages and versions:

`slapt-get --update`

- Install a package, or update it to the latest available version:

`slapt-get --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package:

`slapt-get --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Upgrade all installed packages to their latest available versions:

`slapt-get --upgrade`

- Locate packages by the package name, disk set, or version:

`slapt-get --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Show information about a package:

`slapt-get --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
