---
layout: page
title: common/find (日本語)
description: "ディレクトリツリー下のファイルやディレクトリを再帰的に検索します。"
content_hash: 047604f687290464abef46d507257648571972f2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/find.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/find.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/find.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/find.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

ディレクトリツリー下のファイルやディレクトリを再帰的に検索します。
もっと詳しく: <https://manned.org/find>。

- 拡張子でファイル検索する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- 複数のパス/名前パターンに一致するファイルを検索する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/path/*/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*pattern*</span>`'`

- 大文字小文字を区別しないモードで、指定された名前にマッチするディレクトリを検索する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- 特定のパスを除いて、与えられたパターンにマッチするファイルを検索する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/site-packages/*</span>`'`

- 与えられたサイズ範囲にマッチするファイルを検索し、再帰的な深さを"1"に制限する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- 各ファイルに対してコマンドを実行する (ファイル名にアクセスするにはコマンド内で`{}`を使用):

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l</span>` {} \;`

- 今日変更されたすべてのファイルを検索し、その結果を引数として1つのコマンドに渡す:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -daystart -mtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cvf archive.tar</span>` {} \+`

- 空のファイルまたはディレクトリを検索し、冗長に削除する:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ルートパス</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|d</span>` -empty -delete -print`
