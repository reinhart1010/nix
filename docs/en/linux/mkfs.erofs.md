---
layout: page
title: linux/mkfs.erofs (English)
description: "Create an EROFS filesystem in an image."
content_hash: cc127d6a4a658b3c0a4e22c02f6316b4535e8be9
last_modified_at: 2024-07-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.erofs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.erofs

Create an EROFS filesystem in an image.
More information: <https://erofs.docs.kernel.org/en/latest/>.

- Create an EROFS filesystem based on the root directory:

`mkfs.erofs image.erofs root/`

- Create an EROFS image with a specific UUID:

`mkfs.erofs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` image.erofs root/`

- Create a compressed EROFS image:

`mkfs.erofs -zlz4hc image.erofs root/`

- Create an EROFS image where all files are owned by root:

`mkfs.erofs --all-root image.erofs root/`
