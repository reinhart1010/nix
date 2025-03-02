---
layout: page
title: common/ping (中文)
description: "向网络主机发送 ICMP (ECHO_REQUEST) 数据包。"
content_hash: 18b34541bd67b02a6212a171131be14043c411b0
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ping.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

向网络主机发送 ICMP (ECHO_REQUEST) 数据包。
更多信息：<https://manned.org/ping>.

- Ping 主机：

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- 仅 Ping 主机特定次数：

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- Ping 主机，指定请求之间的间隔（以秒为单位）（默认为 1 秒）：

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">间隔秒数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- Ping 主机而不尝试查找地址的符号名称：

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- Ping 主机并在收到数据包时响铃（如果您的终端支持）：

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- 如果没有收到响应，也显示一条消息：

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>

- Ping 主机，指定 ping 次数、每个数据包的响应超时 (`-W`)和整个 ping 运行的总时间限制 (`-w`) ：

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次数</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">响应超时秒数</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">总的等待超时秒数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机地址</span>
