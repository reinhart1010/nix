---
layout: page
title: linux/debuild (English)
description: "Build a Debian package from source."
content_hash: 7a04c3725f308b0c4643e7b8cf382521c164a39f
last_modified_at: 2024-09-18
related_topics:
  - title: 中文 version
    url: /zh/linux/debuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debuild

Build a Debian package from source.
More information: <https://manned.org/debuild.1>.

- Build the package in the current directory:

`debuild`

- Build a binary package only:

`debuild -b`

- Do not run lintian after building the package:

`debuild --no-lintian`
