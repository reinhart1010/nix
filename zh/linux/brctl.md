---
layout: page
title: linux/brctl (中文)
description: "以太网桥管理。"
content_hash: 11ecca192b7957592c8dbdd0832f45cd67b79d10
related_topics:
  - title: English version
    url: /en/linux/brctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/brctl.html
    icon: bi bi-globe
---
# brctl

以太网桥管理。
更多信息：<https://manned.org/brctl>.

- 显示有关当前现有以太网网桥信息的列表：

`sudo brctl show`

- 创建新的以太网桥接接口：

`sudo brctl add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>

- 删除一个已存在的以太网桥接接口：

`sudo brctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>

- 向现有网桥添加接口:

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名</span>

- 从现有网桥中删除接口：

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名</span>
