---
layout: page
title: linux/slapt-get (English)
description: "An apt like system for Slackware package management."
content_hash: ca5edc718ea52f3a3672c65a20bf3d162ab11608
last_modified_at: 2023-08-26
---
# slapt-get

An apt like system for Slackware package management.
Package sources need to be configured in the slapt-getrc file.
More information: <https://software.jaos.org>.

- Update the list of available packages and versions:

`slapt-get --update`

- Install a package, or update it to the latest available version:

`slapt-get --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package:

`slapt-get --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Upgrade all installed packages to their latest available versions:

`slapt-get --upgrade`

- Locate packages by the package name, disk set, or version:

`slapt-get --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>

- Show information about a package:

`slapt-get --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
