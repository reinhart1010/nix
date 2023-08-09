---
layout: page
title: common/colorls (日本語)
description: "カラー化と Font Awesome アイコンの使用によりターミナルの ls コマンドを美しくした Ruby の gem です。"
content_hash: ee116bb7323c683619819c41498cb01bc8b616ef
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/common/colorls.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># colorls

カラー化と Font Awesome アイコンの使用によりターミナルの ls コマンドを美しくした Ruby の gem です。
詳しくはこちら: <https://github.com/athityakumar/colorls>.

- ファイルを 1 行ずつ表示する:

`colorls -1`

- 隠しファイルを含めた全てのファイルを表示する:

`colorls --all`

- 全てのファイルを長文形式（パーミッション、所有者、サイズ、更新日時）で表示する:

`colorls --long --all`

- ディレクトリのみ表示する:

`colorls --dirs`
