---
layout: page
title: linux/apt-get (中文)
description: "Debian 和 Ubuntu 的软件包管理工具。"
content_hash: af60b85eb67bdd805c13053c43d86a7dd2903544
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Debian 和 Ubuntu 的软件包管理工具。
使用 `apt-cache` 查找包。
更多信息：<https://manpages.debian.org/latest/apt/apt-get.8.html>.

- 更新可用软件包及其版本列表（推荐在其他 `apt-get` 命令运行之前使用）：

`apt-get update`

- 安装一个软件包或更新到最新版本：

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除一个软件包：

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除一个软件包及其配置文件：

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 升级所有已安装软件包到最新版本：

`apt-get upgrade`

- 清理本地仓库 - 移除下载中断后无法再继续下载的（`.deb`）包文件：

`apt-get autoclean`

- 移除所有不再需要的软件包：

`apt-get autoremove`

- 升级已安装的软件包（类似于 `upgrade`），移除过时的软件包并安装额外的软件包以满足新的依赖：

`apt-get dist-upgrade`
