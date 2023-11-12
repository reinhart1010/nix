---
layout: page
title: windows/ipconfig (中文)
description: "显示和管理 Windows 的网络配置。"
content_hash: 8c91fed306e7fde2733e4ec7fd027f986ce64f24
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

显示和管理 Windows 的网络配置。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 显示网络适配器列表：

`ipconfig`

- 显示网络适配器的详细列表：

`ipconfig /all`

- 为一个网络适配器重新获取 IP 地址：

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">适配器</span>

- 为一个网络适配器释放 IP 地址：

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">适配器</span>

- 清除所有 DNS 缓存：

`ipconfig /flushdns`
