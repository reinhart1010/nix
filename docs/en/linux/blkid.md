---
layout: page
title: linux/blkid (English)
description: "Lists all recognized partitions and their Universally Unique Identifier (UUID)."
content_hash: 2bfc2ed4b4f4ab7922123d6587396f5d268aa669
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/blkid.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/blkid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkid

Lists all recognized partitions and their Universally Unique Identifier (UUID).
More information: <https://manned.org/blkid>.

- List all partitions:

`sudo blkid`

- List all partitions in a table, including current mountpoints:

`sudo blkid -o list`
