---
layout: page
title: windows/mklink (日本語)
description: "シンボリックリンクを作成します。"
content_hash: 21f092face0f779ee667d3ec6ab7fec470853987
related_topics:
  - title: English version
    url: /en/windows/mklink.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/mklink.html
    icon: bi bi-globe
---
# mklink

シンボリックリンクを作成します。
詳しくはこちら: <https://docs.microsoft.com/windows-server/administration/windows-commands/mklink>

- ファイルへのシンボリックリンクを作成します:

`mklink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>

- ディレクトリへのシンボリックリンクを作成します:

`mklink /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースディレクトリパス</span>

- ファイルへのハードリンクを作成します:

`mklink /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>

- ディレクトリジャンクションを作成します:

`mklink /j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>
