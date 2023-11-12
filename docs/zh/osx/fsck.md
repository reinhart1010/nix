---
layout: page
title: osx/fsck (中文)
description: "检查或修复文件系统的完整性，运行命令时应卸载文件系统。"
content_hash: efca59ea81f9e17416ed43407cfbcb80c91cc9e7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/fsck.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/fsck.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

检查或修复文件系统的完整性，运行命令时应卸载文件系统。
它是一个包装器，包含 `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, `fsck_udf` 作为可选。
更多信息：<https://ss64.com/osx/fsck.html>.

- 检查文件系统 /dev/sda，报告损坏的块：

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 仅当文件系统 /dev/sda 是干净的时才检查它，报告任何损坏的块并以交互方式让用户选择修复每个块：

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 仅当文件系统 /dev/sda 干净时才检查它，报告任何损坏的块并自动修复它们：

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 检查文件系统 /dev/sda, 报告是否已完全卸载：

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
