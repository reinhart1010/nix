---
layout: page
title: common/git-commit (日本語)
description: "リポジトリにファイルをコミットします。"
content_hash: 0c6d3da4c18b9a0939e988904a6a893f217b8990
last_modified_at: 2023-04-10
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

リポジトリにファイルをコミットします。
詳しくはこちら: <https://git-scm.com/docs/git-commit>.

- メッセージと共に、ステージ済のファイルをリポジトリにコミットする:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- ファイルから読みとったメッセージと共に、ステージ済のファイルをコミットする:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コミットメッセージが書かれたファイルへのパス</span>

- 変更されたファイルを全て自動的にステージし、メッセージと共にコミットする:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- ステージ済のファイルをコミットし、`~/.gitconfig`に設定したGPG鍵で署名する:

`git commit -S -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- 今のステージ済の変更を最後のコミットに付け足し、コミットハッシュを変更する:

`git commit --amend`

- 特定のファイル(ステージ済)だけをコミットする:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス2</span>

- ステージ済のファイルが無くても、コミットを作る:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`" --allow-empty`