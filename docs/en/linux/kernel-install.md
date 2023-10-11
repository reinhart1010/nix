---
layout: page
title: linux/kernel-install (English)
description: "Add and remove kernel and initrd images to and from `/boot`."
content_hash: d732aeae94fb502fbff489e70388763df8c6d362
last_modified_at: 2023-10-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kernel-install

Add and remove kernel and initrd images to and from `/boot`.
More information: <https://manned.org/kernel-install.8>.

- Add kernel and initramfs images to bootloader partition:

`sudo kernel-install add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel-version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel-image</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/initrd-file ...</span>

- Remove kernel from the bootloader partition:

`sudo kernel-install remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel-version</span>

- Show various paths and parameters that have been configured or auto-detected:

`sudo kernel-install inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel-image</span>
