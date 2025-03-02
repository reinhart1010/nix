---
layout: page
title: common/htop (日本語)
description: "実行中のプロセスに関する動的なリアルタイム情報を表示する。 `top` の拡張版。"
content_hash: ef51389f062eb47fff6e56d43df420084f14137e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

実行中のプロセスに関する動的なリアルタイム情報を表示する。 `top` の拡張版。
もっと詳しく: <https://htop.dev/>。

- htop を起動:

`htop`

- 特定のユーザが所有するプロセスを表示する htop を起動する:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザー名</span>

- 指定した `並べ替え項目` でプロセスをソートする (利用可能なオプションは `htop --sort help` を使用する):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">並べ替え項目</span>

- htop 実行中の対話型コマンドを見る:

`?`

- 別のタブに切り替える:

`tab`

- ヘルプを表示する:

`htop --help`
