---
layout: page
title: common/htop (日本語)
description: "実行中のプロセスに関する動的なリアルタイム情報を表示する。 `top` の拡張版。"
content_hash: a812fc8cb5a4138fd1b22b9d7276ad2072139c63
last_modified_at: 2023-11-04
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/htop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># htop

実行中のプロセスに関する動的なリアルタイム情報を表示する。 `top` の拡張版。
詳しくはこちら: <https://htop.dev/>.

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
