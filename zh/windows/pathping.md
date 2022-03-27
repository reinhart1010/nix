---
layout: page
title: windows/pathping (中文)
description: "一种结合了`ping`和`tracert`功能的跟踪路由工具。"
content_hash: e39ec805785e3f64bb080977cf42b2be566e3bd8
related_topics:
  - title: English version
    url: /en/windows/pathping.html
    icon: bi bi-globe
---
# pathping

一种结合了`ping`和`tracert`功能的跟踪路由工具。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/pathping>.

- Ping 并追踪主机的路由：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 不要对主机名执行 IP 地址的反向查找：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -n`

- 指定要搜索目标的最大跃点数（默认值为 30）：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">最大跃点数</span>

- 指定 ping 之间等待的毫秒数（默认值为 240）：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">时间</span>

- 指定每跳的查询数（默认值为 100）：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>

- 强制使用 IPV4：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -4`

- 强制使用 IPV6：

`pathping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -6`

- 显示详细的使用帮助：

`pathping /?`
