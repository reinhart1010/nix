---
layout: page
title: linux/a2query (中文)
description: "在基于 Debian 的操作系统上查看 Apache 运行配置。"
content_hash: e89573c160a42acfecc7e10a8dabe082d384b591
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

在基于 Debian 的操作系统上查看 Apache 运行配置。
更多信息：<https://manned.org/a2query>.

- 列出启用的 Apache 模块：

`sudo a2query -m`

- 查看某个模块是否已安装：

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模块名</span>

- 列出已启用的虚拟主机：

`sudo a2query -s`

- 显示已启用的多进程模块：

`sudo a2query -M`

- 显示 Apache 版本：

`sudo a2query -v`
