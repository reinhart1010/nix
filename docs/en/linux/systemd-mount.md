---
layout: page
title: linux/systemd-mount (English)
description: "Establish and destroy transient mount or auto-mount points."
content_hash: 8889cf3571555d2011744282c3d008e8618e926d
last_modified_at: 2024-01-31
related_topics:
  - title: Nederlands version
    url: /nl/linux/systemd-mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-mount

Establish and destroy transient mount or auto-mount points.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- Mount a file system (image or block device) at `/run/media/system/LABEL` where LABEL is the filesystem label or the device name if there is no label:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_device</span>

- Mount a file system (image or block device) at a specific location:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- List all local, known block devices with file systems that may be mounted:

`systemd-mount --list`

- Create an automount point that mounts the actual file system at the time of first access:

`systemd-mount --automount=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_device</span>

- Unmount one or more devices:

`systemd-mount --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point_or_device1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point_or_device2</span>

- Mount a file system (image or block device) with a specific file system type:

`systemd-mount --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_system_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Mount a file system (image or block device) with additional mount options:

`systemd-mount --options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mount_options</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>
