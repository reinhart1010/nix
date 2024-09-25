---
layout: page
title: linux/pkgctl-build (English)
description: "Build packages inside a clean `chroot`."
content_hash: 9b1610e66a5d37de7ef150cafef6ecc180617bc0
last_modified_at: 2024-09-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/pkgctl-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl build

Build packages inside a clean `chroot`.
More information: <https://manned.org/pkgctl-build.1>.

- Automatically choose the right build script to build packages in a clean `chroot`:

`pkgctl build`

- Manually build packages in a clean `chroot`:

`pkgctl build --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clean`
