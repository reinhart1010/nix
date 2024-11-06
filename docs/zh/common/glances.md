---
layout: page
title: common/glances (中文)
description: "一个跨平台的系统监控工具。"
content_hash: 55192c41e51844b6a7d908a0127993748d9180cc
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/glances.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/glances.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glances.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glances

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
