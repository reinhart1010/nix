---
layout: page
title: common/cat (日本語)
description: "ファイルの出力と連結を行います。"
content_hash: 29953f6b5de07be02843d5d022d9381ee90260c4
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/cat.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cat.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

ファイルの出力と連結を行います。
もっと詳しく: <https://manned.org/cat.1posix>。

- ファイルの内容を標準出力に出力する:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス</span>

- 複数ファイルを連結して1つの出力ファイルにする:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス1 ファイルパス2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイルパス</span>

- 複数ファイルを1つの出力ファイルに追加する:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス1 ファイルパス2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイルパス</span>

- ファイルの内容をバッファリング(一時保存)せずに出力ファイルにコピーする:

`cat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty13</span>

- `stdin`(標準入力)をファイルに書き込む:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス</span>
