---
layout: page
title: linux/btrfs-property (English)
description: "Get, set, or list properties for a given btrfs filesystem object (files, directories, subvolumes, filesystems, or devices)."
content_hash: 237d01f9ff0288354d385da456cc84500ccbb27c
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-property.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs property

Get, set, or list properties for a given btrfs filesystem object (files, directories, subvolumes, filesystems, or devices).
More information: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- List available properties (and descriptions) for the given btrfs object:

`sudo btrfs property list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_object</span>

- Get all properties for the given btrfs object:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_object</span>

- Get the `label` property for the given btrfs filesystem or device:

`sudo btrfs property get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>` label`

- Get all object type-specific properties for the given btrfs filesystem or device:

`sudo btrfs property get -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subvol|filesystem|inode|device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_filesystem</span>

- Set the `compression` property for a given btrfs inode (either a file or directory):

`sudo btrfs property set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/btrfs_inode</span>` compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zstd|zlib|lzo|none</span>
