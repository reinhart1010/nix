---
layout: page
title: common/netstat (日本語)
description: "開いている接続、開いているソケットポートなどのネットワーク関連情報を表示します。"
content_hash: 8cbf7e3f086a0dd7b5eec2da6b4b036c4e33900b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/netstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/netstat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

開いている接続、開いているソケットポートなどのネットワーク関連情報を表示します。
`ss` も参照してください。
もっと詳しく: <https://manned.org/netstat>。

- 全てのポートを一覧表示する:

`netstat --all`

- 全てのリスニングポートを一覧表示する:

`netstat --listening`

- リッスン中のTCPポートを一覧表示する:

`netstat --tcp`

- PIDとプログラム名を表示する:

`netstat --program`

- 情報を連続的に一覧表示する:

`netstat --continuous`

- ルートを一覧表示し、IPアドレスをホスト名に解決しない:

`netstat --route --numeric`

- リッスンしているTCPポートとUDPポートを一覧表示する (+ rootの場合はユーザーとプロセス):

`netstat --listening --program --numeric --tcp --udp --extend`
