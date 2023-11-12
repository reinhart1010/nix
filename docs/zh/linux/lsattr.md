---
layout: page
title: linux/lsattr (中文)
description: "列出 Linux 系统下的文件属性。"
content_hash: 21971a02c3d93026ffd42a524251580d9c33d6f2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lsattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsattr

列出 Linux 系统下的文件属性。
更多信息：<https://manned.org/lsattr>.

- 显示当前目录下文件的属性：

`lsattr`

- 列出指定路径下的文件属性：

`lsattr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- 递归列出当前目录及其子目录中所有文件属性：

`lsattr -R`

- 显示当前目录下所有文件的属性，包括隐藏文件：

`lsattr -a`

- 显示当前目录下的目录属性：

`lsattr -d`
