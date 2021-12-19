---
layout: page
title: linux/bmon (中文)
description: "监控带宽并捕获网络相关统计信息。"
content_hash: 04d9f4e2f25920175b7ab3b7192e5724c8236c53
related_topics:
  - title: English version
    url: /en/linux/bmon.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bmon.html
    icon: bi bi-globe
---
# bmon

监控带宽并捕获网络相关统计信息。
更多信息：<https://github.com/tgraf/bmon>.

- 显示所有接口的列表：

`bmon -a`

- 以每秒位数显示数据传输速率：

`bmon -b`

- 设置策略以定义显示哪些网络接口：

`bmon -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_1,interface_2,interface_3</span>

- 设置计算每个计数器速率的间隔（以秒为单位）：

`bmon -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0</span>
