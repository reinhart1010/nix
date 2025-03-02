---
layout: page
title: common/ag (日本語)
description: "Silver Searcher と呼ばれます。`ack` コマンドに似ていますが、より高速化を目指したコマンドです。"
content_hash: 9ac62601bf9156034403afe49680d9bcf117615f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

Silver Searcher と呼ばれます。`ack` コマンドに似ていますが、より高速化を目指したコマンドです。
もっと詳しく: <https://github.com/ggreer/the_silver_searcher>。

- "foo"という文字列が含まれるファイルを検索し、コンテキスト内でマッチした行を出力する:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 特定のディレクトリ内で、"foo"という文字列が含まれるファイルを検索する:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- "foo"という文字列が含まれるファイルの一覧をリストアップする:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 大文字と小文字を区別せずに、"FOO"という文字列が含まれるファイルを検索し、マッチした行のみ出力する:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- "bar"という名前にマッチするファイルから、"foo"という文字列を検索する:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 正規表現にマッチするコンテンツが含まれるファイルを検索する:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- ファイル名が "foo" に一致するファイルを検索する:

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
