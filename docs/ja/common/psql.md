---
layout: page
title: common/psql (日本語)
description: "PostgreSQL コマンドラインクライアントです。"
content_hash: f681bbf4e6c2161fcecf7f37b47e09b06544f682
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/psql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/psql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# psql

PostgreSQL コマンドラインクライアントです。
もっと詳しく: <https://www.postgresql.org/docs/current/app-psql.html>。

- データベースに接続する。デフォルトでは、現在ログインしているユーザで、ポート5432を使用して、ローカルソケットに接続する:

`psql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース</span>

- 指定ポートで、動作している指定サーバホストのデータベースに、指定ユーザ名で、パスワードプロンプトなしで接続する:

`psql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ポート</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース</span>

- データベースに接続する。ユーザはパスワードの入力を求められる:

`psql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ポート</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース</span>

- 与えられたデータベースに対して、SQLクエリまたはPostgreSQLコマンドを1つ実行する (シェルスクリプトで有用):

`psql -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">クエリ</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース</span>

- 与えられたデータベース上で、ファイルからコマンドを実行する:

`psql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">データベース</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sql</span>
