---
layout: page
title: linux/openvpn3 (中文)
description: "OpenVPN 3 Linux 客户端。"
content_hash: 29d168b6ce9336acd1258b2913af87fb75441b5f
related_topics:
  - title: English version
    url: /en/linux/openvpn3.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># openvpn3

OpenVPN 3 Linux 客户端。
更多信息：<https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- 打开一个新的 VPN 会话：

`openvpn3 session-start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/config.conf</span>

- 列出已建立的会话：

`openvpn3 sessions-list`

- 断开当前建立的以给定配置开始的会话：

`openvpn3 session-manage --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/config.conf</span>` --disconnect`

- 导入 VPN 配置：

`openvpn3 config-import --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/config.conf</span>

- 列出导入的配置：

`openvpn3 configs-list`
