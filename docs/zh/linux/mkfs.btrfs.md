---
layout: page
title: linux/mkfs.btrfs (中文)
description: "创建一个 BTRFS 文件系统。"
content_hash: d0f05886eec698c213d0ab988b35aecf54cbea9d
last_modified_at: 2024-04-23
related_topics:
  - title: English version
    url: /en/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.btrfs

创建一个 BTRFS 文件系统。
默认情况下是 `raid1`，指定了数据块的两份拷贝分布在两个不同的设备上。
更多信息：<https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- 在单个设备上创建一个 btrfs 文件系统：

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 在多个设备上使用 raid1 创建一个 btrfs 文件系统：

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- 为文件系统设置一个标签（可选）：

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
