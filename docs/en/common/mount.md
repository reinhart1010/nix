---
layout: page
title: common/mount (English)
description: "Provides access to an entire filesystem in one directory."
content_hash: e9ef51deb4411192c9e9295120b1dd8740f3bfbb
related_topics:
  - title: Deutsch version
    url: /de/common/mount.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mount.html
    icon: bi bi-globe
---
# mount

Provides access to an entire filesystem in one directory.
More information: <https://manned.org/mount.8>.

- Show all mounted filesystems:

`mount`

- Mount a device to a directory:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Mount a CD-ROM device (with the filetype ISO9660) to `/cdrom` (readonly):

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- Mount all the filesystem defined in `/etc/fstab`:

`mount -a`

- Mount a specific filesystem described in `/etc/fstab` (e.g. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my_drive</span>

- Mount a directory to another directory:

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/old_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_dir</span>
