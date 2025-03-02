---
layout: page
title: windows/cmd (日本語)
description: "Windowsコマンドインタープリター。"
content_hash: 66e589c5d8b20b4f14c76adbc43a59bc938c5b39
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/cmd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmd

Windowsコマンドインタープリター。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>。

- コマンドインタープリターの新しいインスタンスを開始します:

`cmd`

- 指定されたコマンドを実行して終了します:

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- 指定されたコマンドを実行して、インタラクティブシェルに入ります:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- コマンドの出力での「echo」の使用を無効にします:

`cmd /q`

- 環境変数の拡張を有効または無効にします:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- コマンド拡張機能を有効または無効にします:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 出力でUnicodeエンコーディングを使用するように強制します:

`cmd /u`
