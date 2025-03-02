---
layout: page
title: common/git-commit (日本語)
description: "リポジトリにファイルをコミットします。"
content_hash: 2b81c1565acb4dd4e76fe4979aa5801cb5c0b32f
last_modified_at: 2025-03-02
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
  - title: 한국어 version
    url: /ko/common/git-commit.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

リポジトリにファイルをコミットします。
もっと詳しく: <https://git-scm.com/docs/git-commit>。

- メッセージと共に、ステージ済のファイルをリポジトリにコミットする:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- ファイルから読みとったメッセージと共に、ステージ済のファイルをコミットする:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コミットメッセージが書かれたファイルへのパス</span>

- 変更されたファイルを全て自動的にステージし、メッセージと共にコミットする:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`"`

- 今のステージ済の変更を最後のコミットに付け足し、コミットハッシュを変更する:

`git commit --amend`

- 特定のファイル(ステージ済)だけをコミットする:

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス1 ファイルパス2 ...</span>

- ステージ済のファイルが無くても、コミットを作る:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">メッセージ</span>`" --allow-empty`
