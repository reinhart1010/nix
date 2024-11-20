---
layout: page
title: common/quota (中文)
description: "显示用户的磁盘空间使用情况和分配限制。"
content_hash: 4d45cb03adb827a836833ed39325b7f47c9a7090
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/quota.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/quota.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quota

显示用户的磁盘空间使用情况和分配限制。
更多信息：<https://manned.org/quota>.

- 以人类可读的单位显示当前用户的磁盘配额：

`quota -s`

- 详细输出（同时显示未分配存储的文件系统上的配额）：

`quota -v`

- 安静输出（仅显示使用超过配额的文件系统上的配额）：

`quota -q`

- 打印当前用户所属组的配额：

`quota -g`

- 显示其他用户的磁盘配额：

`sudo quota -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>
