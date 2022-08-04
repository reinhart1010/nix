---
layout: page
title: common/zdb (English)
description: "ZFS debugger."
content_hash: 2bd4f7a05bd04c96080532ee30da684df65fbb0e
---
# zdb

ZFS debugger.
More information: <https://manned.org/zdb>.

- Show detailed configuration of all mounted ZFS zpools:

`zdb`

- Show detailed configuration for a specific ZFS pool:

`zdb -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poolname</span>

- Show statistics about number, size and deduplication of blocks:

`zdb -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poolname</span>
