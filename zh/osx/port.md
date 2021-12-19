---
layout: page
title: osx/port (中文)
description: "macOS 包管理器软件（类似 brew）。"
content_hash: 4e8f9a3a061f9af89ba409075747a7a70928c9a3
related_topics:
  - title: English version
    url: /en/osx/port.html
    icon: bi bi-globe
---
# port

macOS 包管理器软件（类似 brew）。

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
