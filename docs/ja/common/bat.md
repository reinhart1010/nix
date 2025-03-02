---
layout: page
title: common/bat (日本語)
description: "ファイルの内容を表示したり、連結したりします。"
content_hash: c59bd2a78f88aefe30d593b0732a6f1f093ee4ae
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/bat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/bat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bat.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bat

ファイルの内容を表示したり、連結したりします。
シンタックスハイライトと Git 統合を備えた `cat`クローンです。
もっと詳しく: <https://github.com/sharkdp/bat>。

- ファイルの内容を、標準出力に出力する:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル</span>

- 複数のファイルの内容を連結して、目的のファイルに書き込む:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ターゲットファイル</span>

- 複数のファイルの内容を連結して、目的のファイルに追記する:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ターゲットファイル</span>

- すべての出力行に番号をつける:

`bat --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル</span>

- JSON ファイルをハイライトする構文:

`bat --language json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JSONファイル</span>

- すべての対応言語を表示する:

`bat --list-languages`
