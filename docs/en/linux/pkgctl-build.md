---
layout: page
title: linux/pkgctl-build (English)
description: "Build packages inside a clean `chroot`."
content_hash: 2fa94f59809e8586e6642960339051e935d9bf74
last_modified_at: 2023-10-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl build

Build packages inside a clean `chroot`.
More information: <https://man.archlinux.org/man/pkgctl-build.1>.

- Automatically choose the right build script to build packages in a clean `chroot`:

`pkgctl build`

- Manually build packages in a clean `chroot`:

`pkgctl build --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --clean`
