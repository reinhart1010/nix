---
layout: page
title: osx/port (中文)
description: "macOS 包管理器软件（类似 brew）。"
content_hash: e9d40e221b106a15b4af19af9f97228c06109418
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/port.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/port.html
    icon: bi bi-globe
tldri18n_status: 2
---
# port

macOS 包管理器软件（类似 brew）。
更多信息：<https://www.macports.org>.

- 搜索包：

`port search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索的包名</span>

- 安装软件包：

`sudo port install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">报名</span>

- 列出已安装的软件包：

`port installed`

- 更新 port 自身，并获取可用包的最新列表：

`sudo port selfupdate`

- 升级过时的软件包：

`sudo port upgrade outdated`

- 删除已安装的软件包的旧版本：

`sudo port uninstall inactive`
