---
layout: page
title: osx/airport (中文)
description: "无线网络配置工具。"
content_hash: 6d3056459896b18892fc0a1bb9ab275be66f2fde
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/osx/airport.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/airport.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/airport.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/airport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airport

无线网络配置工具。
更多信息：<https://ss64.com/osx/airport.html>.

- 显示当前的无线状态信息：

`airport --getinfo`

- 在通道 1 上监察（嗅探）无线流量：

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 扫描可用的无线网络：

`airport --scan`

- 与当前的 Airport 网络脱离连接：

`sudo airport --disassociate`
