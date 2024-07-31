---
layout: page
title: linux/mkfs.erofs (English)
description: "Create an EROFS filesystem in an image."
content_hash: cc127d6a4a658b3c0a4e22c02f6316b4535e8be9
last_modified_at: 2024-07-31
tldri18n_status: 2
---
# mkfs.erofs

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
