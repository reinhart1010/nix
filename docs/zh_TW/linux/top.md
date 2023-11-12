---
layout: page
title: linux/top (中文 (繁體, 台灣))
description: "即時顯示系統執行程序的資訊。"
content_hash: e4c694dabe7423aaf0398ca3aa6a7a2b26c09c0a
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

即時顯示系統執行程序的資訊。
更多資訊：<https://manned.org/top>.

- 啟動 `top`：

`top`

- 不顯示閒置以及殭屍行程：

`top -i`

- 只顯示特定使用者之程序：

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>

- 依照指定領域排序：

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">領域名稱</span>

- 查看程序底下的所有線程：

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序 id</span>

- 僅顯示特定名稱程序的 PID：

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序名稱</span>`)`

- 打開協助頁面：

`?`
