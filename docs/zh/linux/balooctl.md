---
layout: page
title: linux/balooctl (中文)
description: "KDE Plasma 的文件索引和搜索框架。"
content_hash: 2305a84a3ddba52e203a34a8c369be4dbf8faa4c
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/balooctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# balooctl

KDE Plasma 的文件索引和搜索框架。
更多信息：<https://wiki.archlinux.org/index.php/Baloo>.

- 显示索引器状态：

`balooctl status`

- 开启或关闭文件索引器：

`balooctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- 清除索引数据库：

`balooctl purge`

- 挂起文件索引器：

`balooctl suspend`

- 恢复文件索引器：

`balooctl resume`

- 显示 Baloo 占用的磁盘空间大小：

`balooctl indexSize`

- 检查未索引的文件并索引它们：

`balooctl check`

- 显示帮助信息：

`balooctl --help`
