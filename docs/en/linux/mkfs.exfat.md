---
layout: page
title: linux/mkfs.exfat (English)
description: "Create an exfat filesystem inside a partition."
content_hash: 00155e1db324c434c3712b6e43677b5b850b306d
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# mkfs.exfat

Create an exfat filesystem inside a partition.
More information: <https://manned.org/mkfs.exfat>.

- Create an exfat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-name:

`mkfs.exfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-id:

`mkfs.exfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
