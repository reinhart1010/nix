---
layout: page
title: linux/pkgctl-diff (English)
description: "Compare package files using different modes."
content_hash: d76b1b893694b6da5ef8d09fdb946987f0f1f6ad
last_modified_at: 2023-08-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl diff

Compare package files using different modes.
See also: `pkgctl`.
More information: <https://man.archlinux.org/man/pkgctl-diff.1>.

- Compare package files in tar content [l]ist different mode (default):

`pkgctl diff --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in [d]iffoscope different mode:

`pkgctl diff --diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in `.PKGINFO` different mode:

`pkgctl diff --pkginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in `.BUILDINFO` different mode:

`pkgctl diff --buildinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>
