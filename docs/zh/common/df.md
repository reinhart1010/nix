---
layout: page
title: common/df (中文)
description: "显示文件系统磁盘空间使用情况的概览。"
content_hash: f4503591359a865709c58e35ea62fc4277215fff
last_modified_at: 2024-11-27
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

显示文件系统磁盘空间使用情况的概览。
更多信息：<https://manned.org/df.1posix>.

- 以 512 字节为单位显示所有文件系统及其磁盘使用量：

`df`

- 显示包含指定文件或目录的文件系统及其磁盘使用情况：

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 写出空间数据时使用 1024 字节为单位：

`df -k`

- 以可移植的方式显示信息：

`df -P`
