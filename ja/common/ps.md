---
layout: page
title: common/ps (日本語)
description: "実行中のプロセスに関する情報。"
content_hash: abf974b17aeec40f0124160e9a4f9c2187a9369e
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
---
# ps

実行中のプロセスに関する情報。

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
