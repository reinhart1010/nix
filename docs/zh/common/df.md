---
layout: page
title: common/df (中文)
description: "提供文件系统磁盘空间使用情况的概览。"
content_hash: 884358d08db8654b4a983b4e0bc0963e8590e10c
last_modified_at: 2024-01-09
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

提供文件系统磁盘空间使用情况的概览。
更多信息：<https://manned.org/df.1posix>.

- 显示所有文件系统和它们的磁盘使用情况：

`df`

- 以人类可读的形式显示所有文件系统和它们的磁盘使用情况：

`df -h`

- 显示包含给定文件或目录的文件系统及其磁盘使用情况：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 显示索引节点数量的统计数据：

`df -i`

- 显示不包括指定类型的文件系统及其磁盘使用情况：

`df -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>
