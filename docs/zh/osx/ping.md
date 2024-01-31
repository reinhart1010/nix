---
layout: page
title: osx/ping (中文)
description: "向网络主机发送 ICMP 回显请求数据包。"
content_hash: df413fc9ac372ad057e459a3c1193f4520d5b213
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

向网络主机发送 ICMP 回显请求数据包。
更多信息：<https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping 指定的主机：

`ping "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`

- 对主机执行指定定次数的 ping 操作：

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次数</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`

- Ping `主机` , 指定请求之间的间隔（以`秒`为单位）（默认为 1 秒）：

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`

- Ping `主机`, 但不尝试查找地址的符号名：

`ping -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`

- Ping `主机` 并在收到数据包时响铃（如果您的终端支持）：

`ping -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`

- Ping `主机` 并打印接收数据包的时间（此选项是 Apple 的附加项）：

`ping --apple-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机</span>`"`
