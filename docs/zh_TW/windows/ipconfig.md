---
layout: page
title: windows/ipconfig (中文 (繁體, 台灣))
description: "顯示和管理 Windows 的網路設定值。"
content_hash: b139b773006b6e47f732cbfa1c39c70ca2755734
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

顯示和管理 Windows 的網路設定值。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 顯示網路介面卡列表：

`ipconfig`

- 顯示網路介面卡的詳細列表：

`ipconfig /all`

- 為一個網路介面卡重新獲取 IP 地址：

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">介面卡</span>

- 為一個網路介面卡釋放 IP 地址：

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">介面卡</span>

- 清除所有 DNS 快取：

`ipconfig /flushdns`
