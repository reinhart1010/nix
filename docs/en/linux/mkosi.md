---
layout: page
title: linux/mkosi (English)
description: "Tool for building modern, legacy-free Linux images."
content_hash: 6b5ffbcfa7cf462eb1606deb6d1ed706ed3f03e2
last_modified_at: 2023-09-27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkosi

Tool for building modern, legacy-free Linux images.
Part of `systemd`.
More information: <https://manned.org/mkosi>.

- Show current build configuration to verify what would be built:

`mkosi summary`

- Build an image with default settings (if no distribution is selected, the distribution of the host system is used):

`mkosi build --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora|debian|ubuntu|arch|opensuse|...</span>

- Build an image and run an interactive shell in a systemd-nspawn container of the image:

`mkosi shell`

- Boot an image in a virtual machine using QEMU (only supported for disk images or CPIO images when a kernel is provided):

`mkosi qemu`

- Display help:

`mkosi help`
