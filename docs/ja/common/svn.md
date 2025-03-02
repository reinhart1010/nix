---
layout: page
title: common/svn (日本語)
description: "Subversion のコマンドラインクライアントツールです。"
content_hash: 13e219575fa4f60e2537320d06cd0dd5582df3b0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/svn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/svn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svn

Subversion のコマンドラインクライアントツールです。
もっと詳しく: <https://subversion.apache.org>。

- リポジトリから作業コピーをチェックアウトする:

`svn co `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url/to/repository</span>

- リポジトリからの変更を作業コピーに取り込む:

`svn up`

- ファイルやディレクトリをバージョン管理下に置き、リポジトリへの追加をスケジューリングする。これらは次のコミットで追加される:

`svn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パス</span>

- 作業コピーの変更をリポジトリに送信する:

`svn ci -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コミットログメッセージ</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パス</span>`]`

- 過去10リビジョンの変更点を表示し、各リビジョンで変更されたファイルを表示する:

`svn log -vl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- ヘルプを表示する:

`svn help`
