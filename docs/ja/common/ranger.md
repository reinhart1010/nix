---
layout: page
title: common/ranger (日本語)
description: "VI キーバインドのコンソールファイルマネージャー。"
content_hash: ac7e5678590b5c502e27ffaad68ca65462b6537c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ranger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ranger

VI キーバインドのコンソールファイルマネージャー。
詳しくはこちら: <https://github.com/ranger/ranger>

- ranger を起動する:

`ranger`

- ディレクトリのみ表示する:

`ranger --show-only-dirs`

- 設定ディレクトリを変更する:

`ranger --confdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- データディレクトリを変更する:

`ranger --datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 終了時に CPU 使用統計を表示する:

`ranger --profile`
