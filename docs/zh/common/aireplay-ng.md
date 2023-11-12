---
layout: page
title: common/aireplay-ng (中文)
description: "向无线网络注入数据包。"
content_hash: 11f057a2ee2ddf5d67f239f4ff94ff5993ddefc7
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aireplay-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aireplay-ng

向无线网络注入数据包。
`aircrack-ng` 的一部分。
更多信息：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- 向指定的接入点（AP）MAC 地址、客户端 MAC 地址和接口发送指定数量的去关联（disassociate）数据包：

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
