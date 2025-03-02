---
layout: page
title: linux/df (中文)
description: "显示文件系统磁盘空间使用情况的概览。"
content_hash: 64f5136dd95cba9c9f53d2a8aad4606a81ab2f5b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

显示文件系统磁盘空间使用情况的概览。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- 显示磁盘使用情况：

`df`

- 以可读的形式显示磁盘使用情况：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--human-readable</span>

- 显示给定文件或目录的磁盘使用情况：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 包括空闲 inode 数量的统计信息：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--inodes</span>

- 显示文件系统但排除指定的类型：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

- 显示文件系统类型：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--print-type</span>
