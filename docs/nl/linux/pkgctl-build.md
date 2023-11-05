---
layout: page
title: linux/pkgctl-build (Nederlands)
description: "Bouw pakketten in een schone `chroot`."
content_hash: ed55dd1485de98bcc577e2c9700f66a9b8c9b0ae
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/pkgctl-build.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl build

Bouw pakketten in een schone `chroot`.
Meer informatie: <https://man.archlinux.org/man/pkgctl-build.1>.

- Kies automatisch het juiste build script om pakketten in een schone `chroot` te bouwen:

`pkgctl build`

- Bouw pakketten handmatig in een schone `chroot`:

`pkgctl build --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clean`
