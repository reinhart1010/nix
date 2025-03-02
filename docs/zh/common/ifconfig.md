---
layout: page
title: common/ifconfig (中文)
description: "网络接口配置工具。"
content_hash: 63707be50bf9cdc5ef7f992dd0ec3e3748dfe15b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ifconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

网络接口配置工具。
更多信息：<https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- 查看某个网络接口的网络设置：

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名称</span>

- 显示所有接口的详细信息，包括已禁用的接口：

`ifconfig -a`

- 禁用一个接口：

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名称</span>` down`

- 启用一个接口：

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名称</span>` up`

- 为一个接口分配 IP 地址：

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP地址</span>
