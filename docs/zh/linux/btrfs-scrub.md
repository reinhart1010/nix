---
layout: page
title: linux/btrfs-scrub (中文)
description: "清理 btrfs 文件系统以验证数据完整性。"
content_hash: 72e0bd7f065e0001a939f6bb03b0bf15726975e1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

清理 btrfs 文件系统以验证数据完整性。
建议每月运行一次 scrub.
更多信息：<https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- 开始 scrub：

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 显示正在进行或上次完成的 scrub 的状态：

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 取消正在进行的 scrub：

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 恢复先前取消的 scrub：

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 开始擦洗，但要等到 scrub 完成后才能退出：

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>

- 在安静模式下启动 scrub（不打印错误或统计信息）：

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指向挂载点的路径</span>
