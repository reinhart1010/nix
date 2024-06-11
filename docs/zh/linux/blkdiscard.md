---
layout: page
title: linux/blkdiscard (中文)
description: "丢弃存储设备上的设备扇区。对 SSD 有用。"
content_hash: 9cc277a92ac288b36406ca44f46788fc38471002
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/linux/blkdiscard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkdiscard

丢弃存储设备上的设备扇区。对 SSD 有用。
更多信息：<https://manned.org/blkdiscard>.

- 丢弃设备上的所有扇区，删除所有数据：

`blkdiscard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/设备名</span>

- 安全地丢弃设备上的所有块，删除所有数据：

`blkdiscard --secure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/设备名</span>

- 丢弃设备的前 100 MB：

`blkdiscard --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100MB</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/设备名</span>
