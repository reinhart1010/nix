---
layout: page
title: linux/pmount (English)
description: "Mount arbitrary hotpluggable devices as a normal user."
content_hash: f062dbd56470e594a7aca99477dd95ff81bbe9b2
---
# pmount

Mount arbitrary hotpluggable devices as a normal user.
More information: <https://manned.org/pmount>.

- Mount a device below `/media/` (using device as mount point):

`pmount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/to/block/device</span>

- Mount a device with a specific filesystem type to `/media/label`:

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/to/block/device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>

- Mount a CD-ROM (filesystem type ISO9660) in read-only mode:

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Mount an NTFS-formatted disk, forcing read-write access:

`pmount --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` --read-write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Display all mounted removable devices:

`pmount`
