---
layout: page
title: common/ranger (日本語)
description: "VI キーバインドのコンソールファイルマネージャー。"
content_hash: 3a2aba982bbd970c80bd39d8bf7959ba6a02064f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ranger.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ranger.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ranger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ranger

VI キーバインドのコンソールファイルマネージャー。
もっと詳しく: <https://github.com/ranger/ranger>。

- ranger を起動する:

`ranger`

- ディレクトリのみ表示する:

`ranger --show-only-dirs`

- 設定ディレクトリを変更する:

`ranger --confdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- データディレクトリを変更する:

`ranger --datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 終了時に CPU 使用統計を表示する:

`ranger --profile`
