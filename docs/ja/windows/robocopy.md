---
layout: page
title: windows/robocopy (日本語)
description: "堅牢なファイルとフォルダのコピー。"
content_hash: 3670afc11903dbe627270230fd0e2b11eb911f4c
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/robocopy.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/robocopy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/robocopy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/robocopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# robocopy

堅牢なファイルとフォルダのコピー。
デフォルトでは、コピー元とコピー先でタイムスタンプが異なるか、ファイルサイズが異なる場合のみ、ファイルがコピーされます。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/robocopy>。

- すべての `.jpg` と `.bmp` ファイルをあるディレクトリから、別のディレクトリにコピーする:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bmp</span>

- 空のファイルも含めて、すべてのファイルとサブディレクトリをコピーする:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /E`

- ディレクトリをミラー/同期し、ソースにないものを削除し、すべての属性とパーミッションを含める:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /MIR /COPYALL`

- コピー先のファイルより古いソースファイルを除いて、すべてのファイルとサブディレクトリをコピーする:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /E /XO`

- 50MB以上のファイルをコピーする代わりに一覧表示する:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /MIN:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">52428800</span>` /L`

- ネットワーク接続が失われた場合の再開を許可し、再試行を5回、待機時間を15秒に制限する:

`robocopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\destination_directory</span>` /Z /R:5 /W:15`

- ヘルプを表示する:

`robocopy /?`
