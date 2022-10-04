---
layout: page
title: linux/qm-create (English)
description: "Create or restore a virtual machine on QEMU/KVM Virtual Machine Manager."
content_hash: 9f2f4c2d5606b575a25a635cc872235360cfc7c7
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm create

Create or restore a virtual machine on QEMU/KVM Virtual Machine Manager.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Create a virtual machine:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Automatically start the machine after creation:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --start 1`

- Specify the type of operating system on the machine:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --ostype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">win10</span>

- Replace an existing machine (requires archiving it):

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_file.tar</span>` --force 1`

- Specify a script that is executed on specific triggers during machine lifetime:

`qm create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hookscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.pl</span>
