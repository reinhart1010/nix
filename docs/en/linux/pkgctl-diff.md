---
layout: page
title: linux/pkgctl-diff (English)
description: "Compare package files using different modes."
content_hash: 3d49ef9b4d5955287ad57ccbf9a70990857f3bb1
last_modified_at: 2024-09-25
related_topics:
  - title: Nederlands version
    url: /nl/linux/pkgctl-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl diff

Compare package files using different modes.
See also: `pkgctl`.
More information: <https://manned.org/pkgctl-diff.1>.

- Compare package files in tar content [l]ist different mode (default):

`pkgctl diff --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in [d]iffoscope different mode:

`pkgctl diff --diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in `.PKGINFO` different mode:

`pkgctl diff --pkginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>

- Compare package files in `.BUILDINFO` different mode:

`pkgctl diff --buildinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|pkgname</span>
