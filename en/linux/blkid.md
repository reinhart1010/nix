---
layout: page
title: linux/blkid (English)
description: "Lists all recognized partitions and their Universally Unique Identifier (UUID)."
content_hash: 2bfc2ed4b4f4ab7922123d6587396f5d268aa669
related_topics:
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
---
# blkid

Lists all recognized partitions and their Universally Unique Identifier (UUID).
More information: <https://manned.org/blkid>.

- List all partitions:

`sudo blkid`

- List all partitions in a table, including current mountpoints:

`sudo blkid -o list`
