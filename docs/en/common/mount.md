---
layout: page
title: common/mount (English)
description: "Provides access to an entire filesystem in one directory."
content_hash: ad12f0e635ff5855c1d1ee236afda4fa09419c06
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mount.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mount.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount

Provides access to an entire filesystem in one directory.
More information: <https://manned.org/mount.8>.

- Show all mounted filesystems:

`mount`

- Mount a device to a directory:

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Create a specific directory if it does not exist and mount a device to it:

`mount --mkdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Mount a device to a directory for a specific user:

`mount -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_id</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Mount a CD-ROM device (with the filetype ISO9660) to `/cdrom` (readonly):

`mount -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iso9660</span>` -o ro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cdrom</span>

- Mount all the filesystem defined in `/etc/fstab`:

`mount -a`

- Mount a specific filesystem described in `/etc/fstab` (e.g. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my_drive</span>

- Mount a directory to another directory:

`mount --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/old_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/new_dir</span>
