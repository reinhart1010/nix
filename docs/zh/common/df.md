---
layout: page
title: common/df (中文)
description: "提供文件系统磁盘空间使用情况的概览。"
content_hash: cf024eebf0f2bc0eafe79a218213248c73dc4209
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
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># df

提供文件系统磁盘空间使用情况的概览。
更多信息：<https://www.gnu.org/software/coreutils/df>.

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
