---
layout: page
title: linux/blkid (中文)
description: "列出所有已识别的分区及其通用唯一标识符 (UUID)。"
content_hash: 72a0b6acff21e4ddc4c24685a3b94dca49ede5b9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/blkid.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/blkid.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/blkid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkid

列出所有已识别的分区及其通用唯一标识符 (UUID)。
更多信息：<https://manned.org/blkid>.

- 列出所有分区：

`sudo blkid`

- 列出表中的所有分区，包括当前挂载点：

`sudo blkid -o list`
