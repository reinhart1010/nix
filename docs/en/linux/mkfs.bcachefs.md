---
layout: page
title: linux/mkfs.bcachefs (English)
description: "Create a `bcachefs` filesystem inside a partition."
content_hash: 86cea66ee40fc15c04a8173ffb0400cae5bfbde5
last_modified_at: 2024-09-24
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.bcachefs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.bcachefs

Create a `bcachefs` filesystem inside a partition.
More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- Create a `bcachefs` filesystem inside partition 1 on a device (`X`):

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>

- Create a `bcachefs` filesystem with a volume label:

`sudo mkfs.bcachefs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--fs_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX1</span>
