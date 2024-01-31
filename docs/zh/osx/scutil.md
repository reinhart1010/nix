---
layout: page
title: osx/scutil (中文)
description: "管理系统配置参数。"
content_hash: ee0c9d9d8d69688504b39493dd677cc932375f06
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/scutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/scutil.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

管理系统配置参数。
设置配置时必须是 root 权限。
更多信息：<https://keith.github.io/xcode-man-pages/scutil.8.html>.

- 显示 DNS 配置：

`scutil --dns`

- 显示代理配置：

`scutil --proxy`

- 获取计算机名称：

`scutil --get ComputerName`

- 设置计算机名称：

`sudo scutil --set ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的计算机名</span>

- 获取主机名（HostName）：

`scutil --get HostName`

- 设置主机名：

`scutil --set HostName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>
