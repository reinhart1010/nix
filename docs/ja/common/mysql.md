---
layout: page
title: common/mysql (日本語)
description: "MySQL のコマンドラインツールです。"
content_hash: 4814aa53783331897783f1f156fa7f4cc9639a2f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mysql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mysql.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mysql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysql

MySQL のコマンドラインツールです。
もっと詳しく: <https://www.mysql.com/>。

- データベースへの接続:

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース名</span>

- データベースへの接続、ユーザーにはパスワードの入力が求められる:

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザー</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース名</span>

- 別のホスト上のデータベースに接続する:

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベースホスト</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース名</span>

- Unix ソケット経由でのデータベースへの接続:

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソケットファイルへのパス</span>

- スクリプトファイル（バッチファイル）での SQL 文の実行:

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlファイル</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース名</span>

- `mysqldump` で作成したバックアップからデータベースをリストアする（ユーザーはパスワードの入力を求められます）:

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザー</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース名</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">バックアップsqlファイルへのパス</span>

- バックアップからすべてのデータベースを復元する（ユーザーはパスワードの入力を求められます）:

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザー</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">バックアップsqlファイルへのパス</span>
