---
layout: page
title: linux/debuild (English)
description: "Tool to build a Debian package from source."
content_hash: f79f59e1245f5825b2523b331c9118de34077761
related_topics:
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
---
# debuild

Tool to build a Debian package from source.
More information: <https://manpages.debian.org/debuild>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
