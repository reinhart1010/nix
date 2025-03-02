---
layout: page
title: common/z (日本語)
description: "高頻度で利用されるディレクトリを把握し、文字列や正規表現をつかうことでスムーズに移動できるようにします。"
content_hash: b6f57907ab33fa2d8d840a9679e407181941522e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/z.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/z.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/z.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/z.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># z

高頻度で利用されるディレクトリを把握し、文字列や正規表現をつかうことでスムーズに移動できるようにします。
もっと詳しく: <https://github.com/rupa/z>。

- "foo"が名前に含まれるディレクトリに移動する:

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"と"bar"が名前に含まれるディレクトリに移動する:

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- "foo"と最もマッチングするディレクトリに移動する:

`z -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"とマッチングするディレクトリの中で、最も最近アクセスしたディレクトリに移動する:

`z -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- `z`コマンドのデータベースの中で、`foo` にマッチングするディレクトリの一覧を表示する:

`z -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 現在のディレクトリを`z`コマンドのデータベース除去する:

`z -x .`
