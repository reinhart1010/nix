---
layout: page
title: windows/mklink (日本語)
description: "シンボリックリンクを作成します。"
content_hash: 605e2ddc534361c9ce30ea4687dcfac948c91bb1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/mklink.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/mklink.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/mklink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mklink

シンボリックリンクを作成します。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>。

- ファイルへのシンボリックリンクを作成します:

`mklink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>

- ディレクトリへのシンボリックリンクを作成します:

`mklink /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースディレクトリパス</span>

- ファイルへのハードリンクを作成します:

`mklink /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>

- ディレクトリジャンクションを作成します:

`mklink /j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ソースファイルのパス</span>
