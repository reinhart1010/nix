---
layout: page
title: windows/choco-apikey (日本語)
description: "ChocolateyソースのAPIキーを管理します。"
content_hash: 257ea9f8fd1a0cb0ba5e07603ea28c613d2cf38e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco apikey

ChocolateyソースのAPIキーを管理します。
詳しくはこちら: <https://chocolatey.org/docs/commands-apikey>

- ソースとそのAPIキーのリストを表示します:

`choco apikey`

- 特定のソースとそのAPIキーを表示します:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースURL</span>`"`

- ソースのAPIキーを設定します:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースURL</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">APIキー</span>`"`

- ソースのAPIキーを削除します:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースURL</span>`" --remove`
