---
layout: page
title: linux/mkfs.xfs (English)
description: "Create an XFS filesystem inside a partition."
content_hash: 01ccfad9da4ac05a13f712b60cde7528b329428f
last_modified_at: 2024-09-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.xfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.xfs

Create an XFS filesystem inside a partition.
More information: <https://manned.org/mkfs.xfs>.

- Create an XFS filesystem inside partition 1 on a device (`X`):

`sudo mkfs.xfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- Create an XFS filesystem with a volume label:

`sudo mkfs.xfs -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
