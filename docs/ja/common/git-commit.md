---
layout: page
title: common/git-commit (日本語)
description: "リポジトリにファイルをコミットします。"
content_hash: d7bab903a3d2d640311de3299012bfa653ecf109
last_modified_at: 2023-12-29
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
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
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
tldri18n_status: 2
---
# git commit

リポジトリにファイルをコミットします。
詳しくはこちら: <https://git-scm.com/docs/git-commit>

- メッセージと共に、ステージ済のファイルをリポジトリにコミットする:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- ファイルから読みとったメッセージと共に、ステージ済のファイルをコミットする:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コミットメッセージが書かれたファイルへのパス</span>

- 変更されたファイルを全て自動的にステージし、メッセージと共にコミットする:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- 今のステージ済の変更を最後のコミットに付け足し、コミットハッシュを変更する:

`git commit --amend`

- 特定のファイル(ステージ済)だけをコミットする:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス2</span>

- ステージ済のファイルが無くても、コミットを作る:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`" --allow-empty`
