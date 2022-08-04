---
layout: page
title: common/ls (日本語)
description: "ディレクトリの内容を一覧表示します。"
content_hash: ab1e6678a3a88cc9852b726b5c6a66cbc1a81c0b
related_topics:
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ls

ディレクトリの内容を一覧表示します。
詳しくはこちら: <https://www.gnu.org/software/coreutils/ls>

- ファイルを1行ごとに一覧表示:

`ls -1`

- 隠しファイルを含むすべてのファイルを一覧表示:

`ls -a`

- すべてのファイルを一覧表示し、ディレクトリ名の最後に `/` を付加する:

`ls -F`

- 全ファイルを長い形式（パーミッション、所有者、サイズ、修正日）で一覧表示します:

`ls -la`

- サイズを人間が読みやすい単位（KiB、MiB、GiB）で表示した長い形式での一覧表示:

`ls -lh`

- サイズ順（降順）に並べた長い形式での一覧表示:

`ls -lS`

- すべてのファイルの長い形式でのリストで、更新日が古いものから順に表示されます:

`ls -ltr`
