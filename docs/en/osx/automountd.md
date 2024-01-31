---
layout: page
title: osx/automountd (English)
description: "An automatic mount/unmount daemon for `autofs`. Started on demand by `launchd`."
content_hash: 6129a74558b464d153831e74be53fda1f26f758c
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/automountd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/automountd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# automountd

An automatic mount/unmount daemon for `autofs`. Started on demand by `launchd`.
It should not be invoked manually.
More information: <https://keith.github.io/xcode-man-pages/automountd.8.html>.

- Start the daemon:

`automountd`

- Log more details to `syslog`:

`automountd -v`
