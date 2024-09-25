---
layout: page
title: linux/genfstab (English)
description: "Arch Linux install script to generate output suitable for addition to an fstab file."
content_hash: 972104dcc7cf7777da7593b5b6453540307f43ab
last_modified_at: 2024-09-25
tldri18n_status: 2
---
# genfstab

Arch Linux install script to generate output suitable for addition to an fstab file.
More information: <https://manned.org/genfstab.8>.

- Display an fstab compatible output based on a volume label:

`genfstab -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Display an fstab compatible output based on a volume UUID:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- A usual way to generate an fstab file, requires root permissions:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/etc/fstab</span>

- Append a volume into an fstab file to mount it automatically:

`genfstab -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>` | sudo tee -a /etc/fstab`
