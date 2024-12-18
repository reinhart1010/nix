---
layout: page
title: common/echo (日本語)
description: "与えられた引数を表示します。"
content_hash: e499d989cc6854305f759cc77041bd06383b4fa9
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># echo

与えられた引数を表示します。
詳しくはこちら: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>

- テキストメッセージを印刷する。備考: 引用符は任意:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- 環境変数のメッセージを表示する:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パスは $PATH です。</span>`"`

- メッセージを最後の改行なしで表示する:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- ファイルにメッセージを追加する:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル.txt</span>

- バックスラッシュエスケープ（特殊文字）の解釈を可能にする:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">カラム 1\tカラム 2</span>`"`
