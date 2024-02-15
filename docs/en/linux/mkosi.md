---
layout: page
title: linux/mkosi (English)
description: "Build modern, legacy-free Linux images."
content_hash: 826b3cd5b65a0f47d95798e283427ffc232db6d4
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# mkosi

Build modern, legacy-free Linux images.
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
