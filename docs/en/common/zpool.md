---
layout: page
title: common/zpool (English)
description: "Manage ZFS pools."
content_hash: d7f54fadfa9acf17a03b0625aad3b9846c9debe3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zpool

Manage ZFS pools.
More information: <https://manned.org/zpool>.

- Show the configuration and status of all ZFS zpools:

`zpool status`

- Check a ZFS pool for errors (verifies the checksum of EVERY block). Very CPU and disk intensive:

`zpool scrub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- List zpools available for import:

`zpool import`

- Import a zpool:

`zpool import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- Export a zpool (unmount all filesystems):

`zpool export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- Show the history of all pool operations:

`zpool history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- Create a mirrored pool:

`zpool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk2</span>` mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disk4</span>

- Add a cache (L2ARC) device to a zpool:

`zpool add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>` cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cache_disk</span>
