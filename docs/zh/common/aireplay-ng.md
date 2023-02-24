---
layout: page
title: common/aireplay-ng (中文)
description: "向无线网络注入数据包。"
content_hash: 11f057a2ee2ddf5d67f239f4ff94ff5993ddefc7
last_modified_at: 2023-02-24
related_topics:
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aireplay-ng

向无线网络注入数据包。
`aircrack-ng` 的一部分。
更多信息：<https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- 向指定的接入点（AP）MAC 地址、客户端 MAC 地址和接口发送指定数量的去关联（disassociate）数据包：

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
