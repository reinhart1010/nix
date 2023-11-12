---
layout: page
title: linux/iptables (中文)
description: "可用于配置 Linux 内核防火墙提供的过滤表、规则链和规则的程序。"
content_hash: 0d8234007ce3d3d8379fd02b3375102ff4038481
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/iptables.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iptables

可用于配置 Linux 内核防火墙提供的过滤表、规则链和规则的程序。
更多信息：<https://manned.org/iptables>.

- 查看过滤表的规则链、规则以及数据包/字节计数器：

`sudo iptables -vnL`

- 设定规则链策略规则：

`sudo iptables -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则链</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则</span>

- 追加规则到 IP 的规则链策略：

`sudo iptables -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则链</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则</span>

- 追加规则到 IP 的规则链策略（考虑协议与端口）：

`sudo iptables -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则链</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">协议</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>` -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则</span>

- 删除规则链中的规则：

`sudo iptables -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则链</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则所在行号</span>

- 将指定过滤表的 iptables 配置保存到文件中：

`sudo iptables-save -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">过滤表名</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iptables_文件路径</span>

- 从文件中还原 iptables 配置：

`sudo iptables-restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iptables_文件路径</span>
