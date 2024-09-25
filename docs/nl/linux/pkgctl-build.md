---
layout: page
title: linux/pkgctl-build (Nederlands)
description: "Bouw pakketten in een schone `chroot`."
content_hash: 8b291b714cb340d98694c3eaface2748a83c92f2
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pkgctl-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl build

Bouw pakketten in een schone `chroot`.
Meer informatie: <https://manned.org/pkgctl-build.1>.

- Kies automatisch het juiste build script om pakketten in een schone `chroot` te bouwen:

`pkgctl build`

- Bouw pakketten handmatig in een schone `chroot`:

`pkgctl build --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clean`
