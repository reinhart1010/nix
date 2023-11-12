---
layout: page
title: common/history (日本語)
description: "コマンドラインの履歴です。"
content_hash: 6d340509f20e3399fdf0c84d07b73fbcf7136a4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history

コマンドラインの履歴です。
詳しくはこちら: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>

- コマンドの履歴一覧を行番号付きで表示する:

`history`

- 直近の20個のコマンドを表示する (`zsh` では20個目から始まるすべてのコマンドを表示する):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- コマンド履歴のリストを消去する (現在の `bash` シェルに対してのみ):

`history -c`

- コマンド履歴ファイルを現在の `bash` シェルのコマンド履歴で上書きする (履歴を削除するために `history -c` と組み合わせることがよくあります):

`history -w`

- 指定されたオフセットの履歴エントリーを削除する:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">オフセット</span>
