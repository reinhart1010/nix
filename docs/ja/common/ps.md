---
layout: page
title: common/ps (日本語)
description: "実行中のプロセスに関する情報。"
content_hash: 0338f1dfb00cb8049ff7c1f223b555dece279b3e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

実行中のプロセスに関する情報。
詳しくはこちら: <https://manned.org/ps>

- 実行中のプロセスをすべてリストアップ:

`ps aux`

- 実行中のすべてのプロセスを、完全なコマンド文字列を含めて一覧表示する:

`ps auxww`

- 文字列にマッチするプロセスを検索する:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字列</span>

- 現在のユーザーのすべてのプロセスを完全なフォーマットで表示する:

`ps --user $(id -u) -F`

- カレントユーザーの全プロセスをツリー状にリストアップ:

`ps --user $(id -u) f`

- プロセスの親 pid を取得する:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- プロセスをメモリ消費量でソート:

`ps --sort size`
