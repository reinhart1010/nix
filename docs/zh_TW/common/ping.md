---
layout: page
title: common/ping (中文 (繁體, 台灣))
description: "向網路主機發送 ICMP ECHO_REQUEST 封包。"
content_hash: 4bb0599e0d4d5deeeab2efdb875e93883d96620a
last_modified_at: 2024-08-03
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ping

向網路主機發送 ICMP ECHO_REQUEST 封包。
更多資訊：<https://manned.org/ping>.

- Ping 主機：

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主機</span>

- 對主機執行特定次數的 ping 操作：

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">次數</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主機</span>

- Ping 主機，指定發送間隔（以秒為單位）（預設為 1 秒）：

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒數</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主機</span>

- Ping 主機，只以數字形式輸出，不嘗試查找名稱：

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主機</span>

- Ping 主機並在收到封包時響鈴（如果您的終端支援）：

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主機</span>

- 如果未收到回應，也會顯示訊息：

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
