---
layout: page
title: linux/brctl (中文)
description: "以太网桥管理。"
content_hash: 3f61197ff86cdc06e3fbdc1ad95d475c6571f203
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/brctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/brctl.html
    icon: bi bi-globe
tldri18n_status: 2
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

- 向现有网桥添加接口：

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名</span>

- 从现有网桥中删除接口：

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网桥名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名</span>
