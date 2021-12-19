---
layout: page
title: windows/choco-apikey (日本語)
description: "ChocolateyソースのAPIキーを管理します。"
content_hash: 2d4ae2af89c71544d8652ebd489e08424629b02e
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
---
# choco-apikey

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
