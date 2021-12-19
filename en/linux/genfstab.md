---
layout: page
title: linux/genfstab (English)
description: "Arch Linux install script to generate output suitable for addition to an fstab file."
content_hash: 5f115361468fa78aae502d32e2512f06f00557c0
---
# genfstab

Arch Linux install script to generate output suitable for addition to an fstab file.
More information: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8>.

- Display an fstab compatible output based on a volume label:

`genfstab -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Display an fstab compatible output based on a volume UUID:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- A usual way to generate an fstab file, requires root permissions:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/etc/fstab</span>

- Append a volume into an fstab file to mount it automatically:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>` | sudo tee -a /etc/fstab`
