---
layout: page
title: windows/xcopy (日本語)
description: "ファイルとディレクトリツリーをコピーします。"
content_hash: fbff91792b11c8a5a319c1f063fba9ca54cc0d54
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/xcopy.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/xcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/xcopy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/xcopy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/xcopy.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/xcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/xcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcopy

ファイルとディレクトリツリーをコピーします。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>。

- ファイル(単独または複数)を指定された宛先にコピーする:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>

- コピーの前に、コピーするファイルを一覧表示する:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /p`

- ファイルを除いてディレクトリ構造だけをコピーする:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /t`

- コピー時に、空のディレクトリを含める:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /e`

- コピー元のACLを、コピー先に残す:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /o`

- ネットワーク接続が切れたときに、再開できるようにする:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /z`

- コピー先にファイルが存在する場合、プロンプトを表示しない:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /y`

- ヘルプを表示する:

`xcopy /?`
