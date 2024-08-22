---
layout: page
title: linux/wg (中文)
description: "管理 WireGuard 接口配置。"
content_hash: 49ebccc87af5da773d2c86c1d55ee16264450169
last_modified_at: 2024-08-22
related_topics:
  - title: English version
    url: /en/linux/wg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/wg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wg

管理 WireGuard 接口配置。
更多信息：<https://www.wireguard.com/quickstart/>.

- 检查当前激活接口的状态：

`sudo wg`

- 生成新的私钥：

`wg genkey`

- 从私钥生成公钥：

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/公钥</span>

- 同时生成公钥和私钥：

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/公钥</span>

- 展示 WireGuard 接口的当前配置：

`sudo wg showconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wg0</span>
