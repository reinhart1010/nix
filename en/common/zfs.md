---
layout: page
title: common/zfs (English)
description: "Manage ZFS filesystems."
content_hash: 23dd92783d4c8a10d47ea8199f1014d98a459e2e
---
# zfs

Manage ZFS filesystems.
More information: <https://manned.org/zfs>.

- List all available zfs filesystems:

`zfs list`

- Create a new ZFS filesystem:

`zfs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name/filesystem_name</span>

- Delete a ZFS filesystem:

`zfs destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name/filesystem_name</span>

- Create a Snapshot of a ZFS filesystem:

`zfs snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name/filesystem_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>

- Enable compression on a filesystem:

`zfs set compression=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name/filesystem_name</span>

- Change mountpoint for a filesystem:

`zfs set mountpoint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my/mount/path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name/filesystem_name</span>
