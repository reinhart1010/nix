---
layout: page
title: common/glances (中文)
description: "一个跨平台的系统监控工具。"
content_hash: 55192c41e51844b6a7d908a0127993748d9180cc
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/glances.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/glances.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glances

一个跨平台的系统监控工具。
更多信息：<https://nicolargo.github.io/glances/>.

- 启动 glances，实时显示系统状态：

`glances`

- 以网页服务器模式启动，在浏览器中查看监控数据：

`glances -w`

- 以服务器模式启动，允许其他 glances 客户端连接以查看数据：

`glances -s`

- 作为客户端连接到 glances 服务器：

`glances -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名或IP地址</span>

- 在（网页）服务器模式下启用密码保护：

`glances -s --password`
