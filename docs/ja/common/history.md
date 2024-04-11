---
layout: page
title: common/history (日本語)
description: "コマンドラインの履歴です。"
content_hash: f5557d190942a15ca1010a045effd6fe728eb149
last_modified_at: 2024-04-11
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># history

コマンドラインの履歴です。
詳しくはこちら: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>

- コマンドの履歴一覧を行番号付きで表示する:

`history`

- 直近の20個のコマンドを表示する (Zsh では20個目から始まるすべてのコマンドを表示する):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- コマンド履歴のリストを消去する (現在の Bash シェルに対してのみ):

`history -c`

- コマンド履歴ファイルを現在の Bash シェルのコマンド履歴で上書きする (履歴を削除するために `history -c` と組み合わせることがよくあります):

`history -w`

- 指定されたオフセットの履歴エントリーを削除する:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">オフセット</span>
