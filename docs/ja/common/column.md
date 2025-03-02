---
layout: page
title: common/column (日本語)
description: "`stdin` またはファイルを複数の列にフォーマットします。"
content_hash: 31d6a559ee37ba41697c31fdab10793549a28409
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/column.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/column.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# column

`stdin` またはファイルを複数の列にフォーマットします。
デフォルトの区切り文字は空白文字です。
もっと詳しく: <https://manned.org/column>。

- 30文字幅の表示用にコマンドの出力をフォーマットする:

`printf "header1 header2\nbar foo\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- カラムを自動的に分割し、表形式に自動整列する:

`printf "header1 header2\nbar foo\n" | column --table`

- `table`オプションにカラムの区切り文字を指定する(CSVの場合は","など) (デフォルトは空白文字):

`printf "header1,header2\nbar,foo\n" | column --table --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- 列を埋める前に行を埋める:

`printf "header1\nbar\nfoobar\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` --fillrows`
