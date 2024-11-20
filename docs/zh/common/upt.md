---
layout: page
title: common/upt (中文)
description: "统一的界面，用于管理各种操作系统上的软件包，例如 Windows、许多 Linux 发行版、macOS、FreeBSD，甚至 Haiku。"
content_hash: 43dd5f748124be55882e836b4f522fa2ad3382f9
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/upt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/upt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/upt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# upt

统一的界面，用于管理各种操作系统上的软件包，例如 Windows、许多 Linux 发行版、macOS、FreeBSD，甚至 Haiku。
它需要安装本机操作系统的软件包管理器。
请参阅：`flatpak`、`brew`、`scoop`、`apt`、`dnf`.
更多信息：<https://github.com/sigoden/upt>.

- 更新可用软件包的列表：

`upt update`

- 搜索指定的软件包：

`upt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索软件包关键词</span>

- 显示某个软件包的信息：

`upt info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 安装指定的软件包：

`upt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除指定的软件包：

`upt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 升级所有已安装的软件包：

`upt upgrade`

- 升级指定的软件包：

`upt upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 列出已安装的软件包：

`upt list`
