---
layout: page
title: common/scrapy (日本語)
description: "ウェブクローリングのフレームワークです。"
content_hash: a8568dd361f1bc579df33f8914176efb2cf328c1
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/scrapy.html
    icon: bi bi-globe
---
# scrapy

ウェブクローリングのフレームワークです。
詳しくはこちら: <https://scrapy.org>.

- プロジェクトを作成する:

`scrapy startproject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">プロジェクト名</span>

- スパイダーを作成する (プロジェクトのディレクトリ内での実行):

`scrapy genspider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">スパイダー名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ウェブサイトのドメイン名</span>

- スパイダーを編集する (プロジェクトのディレクトリ内での実行):

`scrapy edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">スパイダー名</span>

- スパイダーを実行する (プロジェクトのディレクトリ内での実行):

`scrapy crawl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">スパイダー名</span>

- Scrapyが見るようにWebページを取得しソースを`stdout`(標準出力)に表示する:

`scrapy fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Scrapyが見ているようにデフォルトブラウザ内でウェブページを開く(より応答に忠実であるようにするためにJavaScriptを無効化している):

`scrapy view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- URL用のScrapyシェルを開き、Python(もしくは可能であればIPython)シェル内でページソースとの対話式でのやり取りを可能にする:

`scrapy shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
