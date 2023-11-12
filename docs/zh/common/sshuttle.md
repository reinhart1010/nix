---
layout: page
title: common/sshuttle (中文)
description: "通过 ssh 连接传输流量的透明代理服务器。"
content_hash: 478ebaeaf8f30763af34741ba4bafe0c53944f7f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sshuttle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sshuttle

通过 ssh 连接传输流量的透明代理服务器。
不需要管理员或远程 ssh 服务器上的任何特殊设置。
更多信息：<https://manned.org/sshuttle>.

- 通过远程 ssh 服务器转发所有 IPv4 TCP 流量：

`sshuttle --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- 转发所有 IPv4 TCP 和 DNS 流量：

`sshuttle --dns --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>

- 使用 tproxy 方法转发所有 IPv4 和 IPv6 流量：

`sudo sshuttle --method=tproxy --remote=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0/0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">::/0</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你本地 IP 地址</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSH 服务器的 IP 地址</span>
