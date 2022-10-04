---
layout: page
title: windows/ipconfig (日本語)
description: "Windowsのネットワーク構成を表示および管理します。"
content_hash: ad5ac3079732714814beb0d1d8f38efa5b9f876b
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
---
# ipconfig

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
