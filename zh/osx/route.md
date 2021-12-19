---
layout: page
title: osx/route (中文)
description: "手动操作路由表。"
content_hash: 452e2311b6f5661c89ec6f76a8fb5bf39d825c49
related_topics:
  - title: English version
    url: /en/osx/route.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/route.html
    icon: bi bi-globe
---
# route

手动操作路由表。
需要 root 权限。

- 通过网关向目标添加路由：

`sudo route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路由 ip 地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网关地址</span>

- 通过网关向 子网 / 24 添加路由：

`sudo route add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子网 ip</span>`/24 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网关地址</span>

- 在测试模式下运行（不做任何操作，只打印）：

`sudo route -t add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路由 ip 地址</span>`/24 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网关地址</span>

- 删除所有路由：

`sudo route flush`

- 删除特定路由：

`sudo route delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路由 ip 地址</span>`/24`

- 查找并显示目标的路由（主机名或 IP 地址）：

`sudo route get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>
