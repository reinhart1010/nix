---
layout: page
title: linux/debuild (English)
description: "Build a Debian package from source."
content_hash: 0fb0938ac0e47cd12cf22bf06159b2fa827f383c
last_modified_at: 2024-02-15
related_topics:
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debuild

Build a Debian package from source.
More information: <https://manpages.debian.org/latest/devscripts/debuild.1.en.html>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
