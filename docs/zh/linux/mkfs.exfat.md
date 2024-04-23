---
layout: page
title: linux/mkfs.exfat (中文)
description: "在分区内创建一个 exFAT 文件系统。"
content_hash: e075b31709bbfef9dcf941eb5a97eeb391439fd9
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.exfat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.exfat

在分区内创建一个 exFAT 文件系统。
更多信息：<https://manned.org/mkfs.exfat>.

- 在设备 b 的分区 1 内创建一个 exFAT 文件系统（`sdb1`）：

`mkfs.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷名的文件系统：

`mkfs.exfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 创建一个带有卷 ID 的文件系统：

`mkfs.exfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
