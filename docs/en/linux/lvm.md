---
layout: page
title: linux/lvm (English)
description: "Manage physical volumes, volume groups, and logical volumes using the Logical Volume Manager (LVM) interactive shell."
content_hash: ee3c6487b660cc0271052d9ae569d82b9189c5ce
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# lvm

Manage physical volumes, volume groups, and logical volumes using the Logical Volume Manager (LVM) interactive shell.
More information: <https://manned.org/lvm>.

- Start the Logical Volume Manager interactive shell:

`sudo lvm`

- Initialize a drive or partition to be used as a physical volume:

`sudo lvm pvcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Display information about physical volumes:

`sudo lvm pvdisplay`

- Create a volume group called vg1 from the physical volume on `/dev/sdXY`:

`sudo lvm vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Display information about volume groups:

`sudo lvm vgdisplay`

- Create a logical volume with size 10G from volume group vg1:

`sudo lvm lvcreate -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>

- Display information about logical volumes:

`sudo lvm lvdisplay`

- Display help for a specific command:

`lvm help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
