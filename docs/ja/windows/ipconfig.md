---
layout: page
title: windows/ipconfig (日本語)
description: "Windowsのネットワーク構成を表示および管理します。"
content_hash: ad5ac3079732714814beb0d1d8f38efa5b9f876b
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
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

Windowsのネットワーク構成を表示および管理します。
詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>

- ネットワークアダプタのリストを表示します:

`ipconfig`

- ネットワークアダプタの詳細なリストを表示します:

`ipconfig /all`

- ネットワークアダプタのIPアドレスを更新します:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- ネットワークアダプタのIPアドレスを解放します:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- DNSキャッシュからすべてのデータを削除します:

`ipconfig /flushdns`
