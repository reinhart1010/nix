---
layout: page
title: linux/ip (日本語)
description: "ルーティング、デバイス、ポリシールーティング、トンネルの表示/操作。"
content_hash: b8ff8a14a0dbf6fed6babd4c1f00d97645a0df6f
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/ip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ip.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip

ルーティング、デバイス、ポリシールーティング、トンネルの表示/操作。
`address` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
もっと詳しく: <https://www.manned.org/ip.8>。

- インターフェースの詳細情報を表示する:

`ip address`

- 簡単なネットワークレイヤの情報を持つインターフェースを一覧表示する:

`ip -brief address`

- リンク層の簡単な情報を持つインターフェースを一覧表示する:

`ip -brief link`

- ルーティングテーブルを表示する:

`ip route`

- ネイバー(ARP テーブル)を表示する:

`ip neighbour`

- インターフェースを up/down する:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">インターフェース</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- インターフェースにIPアドレスを追加/削除する:

`ip addr add/del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">インターフェース</span>

- デフォルトルートを追加する:

`ip route add default via `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">インターフェース</span>
