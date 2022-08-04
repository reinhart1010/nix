---
layout: page
title: linux/apt (中文)
description: "基于 Debian 的发行版上的软件包管理工具。"
content_hash: 36732ab2bb89d640a58119ffa5f4f51dc02f9edc
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
---
# apt

基于 Debian 的发行版上的软件包管理工具。
在 Ubuntu 16.04 及之后版本推荐用它代替 `apt-get` 。
更多信息：<https://manpages.debian.org/latest/apt/apt.8.html>.

- 更新可用软件包及其版本列表（推荐在运行其他 apt 命令前首先运行该命令）：

`sudo apt update`

- 查找指定软件包：

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 显示关于指定软件包的信息：

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 安装指定软件包或将指定软件包更新到最新版本：

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除指定软件包（使用 `purge` 同时移除其配置文件）：

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 将所有已安装软件包更新到最新可用版本：

`sudo apt upgrade`

- 列出所有软件包：

`apt list`

- 列出已安装的软件包：

`apt list --installed`
