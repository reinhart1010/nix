---
layout: page
title: windows/find (日本語)
description: "1つ以上のファイルで指定された文字列を検索します。"
content_hash: 66a369ff9639c4ab1a88ba46d7b620e91b61e277
related_topics:
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
---
# find

1つ以上のファイルで指定された文字列を検索します。
詳しくはこちら: <https://docs.microsoft.com/windows-server/administration/windows-commands/find>

- 指定された文字列を含む行を検索します:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字列</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルまたはディレクトリのパス</span>

- 指定された文字列を含まない行を表示します:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字列</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルまたはディレクトリのパス</span>` /v`

- 指定された文字列を含む行数を表示します:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字列</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルまたはディレクトリのパス</span>` /c`

- 行リストとともに行番号を表示します:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文字列</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルまたはディレクトリのパス</span>` /n`
