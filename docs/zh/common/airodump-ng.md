---
layout: page
title: common/airodump-ng (中文)
description: "捕获数据包并显示有关无线网络的信息。"
content_hash: 4bf63ed620068d7896de640ad1e779faf87f0adb
last_modified_at: 2023-11-04
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
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
---
# airodump-ng

捕获数据包并显示有关无线网络的信息。
`aircrack-ng` 的一部分。
更多信息： <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- 捕获数据包并显示有关无线网络的信息：

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- 捕获数据包并显示有关无线网络的信息，给定 MAC 地址和信道，并将输出保存到文件中：

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">信道</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
