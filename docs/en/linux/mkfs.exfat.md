---
layout: page
title: linux/mkfs.exfat (English)
description: "Creates an exfat filesystem inside a partition."
content_hash: c175bd5d46c49d9b1ebecf39c47312a7de91bcf9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mkfs.exfat

Creates an exfat filesystem inside a partition.
More information: <https://manned.org/mkfs.exfat>.

- Create an exfat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-name:

`mkfs.exfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Create filesystem with a volume-id:

`mkfs.exfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
