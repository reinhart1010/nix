---
layout: page
title: linux/debuild (English)
description: "Tool to build a Debian package from source."
content_hash: 5751b6454bc841b490734147e4ca47be6b551b9c
last_modified_at: 2023-05-14
related_topics:
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
---
# debuild

Tool to build a Debian package from source.
More information: <https://manpages.debian.org/latest/devscripts/debuild.1.en.html>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
