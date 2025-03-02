---
layout: page
title: windows/ipconfig (日本語)
description: "Windowsのネットワーク構成を表示および管理します。"
content_hash: 6c017d9cbc69dbc3e919f129e993bb3104bb4d19
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/ipconfig.html
    icon: bi bi-globe
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
  - title: 한국어 version
    url: /ko/windows/ipconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/ipconfig.html
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
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>。

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
