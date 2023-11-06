---
layout: page
title: common/git (日本語)
description: "分散型バージョン管理システム"
content_hash: 92df3479a9177f418c880290fb0946a0a5f0f1e5
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git.html
    icon: bi bi-globe
---
# git

分散型バージョン管理システム
いくつかのサブコマンドがあります。例えば `commit`, `add`, `branch`, `checkout`, `push`, などです。 これらには使用方法についての独自のドキュメントがあり、 `tldr git subcommand` で見ることができます。
詳しくはこちら: <https://git-scm.com/>

- Gitのバージョンを確認する:

`git --version`

- Git全体のヘルプを見る:

`git --help`

- Gitのサブコマンドのヘルプを見る (例えば `clone`, `add`, `push`, `log`, など):

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サブコマンド</span>

- Gitのサブコマンドを実行する:

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サブコマンド</span>

- Gitのサブコマンドを、任意のリポジトリのルートパスを指定して実行する:

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サブコマンド</span>

- Gitのサブコマンドを、指定された設定値で実行する:

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">値</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サブコマンド</span>
