---
layout: page
title: linux/aptitude (中文)
description: "Debian 和 Ubuntu 上的软件包管理工具。"
content_hash: f8073fa8a05bf06e02c3f38c11f746cf39fba388
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Debian 和 Ubuntu 上的软件包管理工具。
更多信息：<https://manned.org/aptitude.8>.

- 同步可用软件包及其版本列表，在运行后续 aptitude 命令前，应该首先运行该命令：

`aptitude update`

- 安装一个新的软件包及其依赖：

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 查找一个软件包：

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 查找一个已安装的软件包（`?installed` 是一个 aptitude 搜索项）：

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>`)'`

- 移除一个软件包并移除所有依赖它的软件包：

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 更新已安装软件包到最新版本：

`aptitude upgrade`

- 更新已安装的软件包（类似于 `aptitude upgrade` 命令），移除过时的软件包并安装额外的软件包以满足新的软件包依赖项：

`aptitude full-upgrade`

- 锁定一个已安装的软件包以便阻止它自动升级：

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>`)'`
