---
layout: page
title: common/airodump-ng (中文)
description: "捕获数据包并显示有关无线网络的信息。"
content_hash: 679ba03d575fc111fd7f7b6cec1964ad84eaa508
last_modified_at: 2024-06-24
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airodump-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airodump-ng

捕获数据包并显示有关无线网络的信息。
`aircrack-ng` 的一部分。
更多信息：<https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- 捕获数据包并显示有关无线网络的信息：

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网络接口</span>

- 捕获数据包并显示关于 5GHz 频段无线网络的信息：

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网络接口</span>` --band a`

- 捕获数据包并显示关于 2.4GHz 和 5GHz 频段无线网络的信息：

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网络接口</span>` --band abg`

- 捕获数据包并显示有关无线网络的信息，给定 MAC 地址和信道，并将输出保存到文件中：

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">信道</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网络接口</span>
