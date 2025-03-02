---
layout: page
title: windows/more (日本語)
description: "`stdin` またはファイルからのページ分割された出力を表示します。"
content_hash: 0d9a4a7cfec39b41d5b36ce36ffad58a6151c620
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/more.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/more.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/more.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

`stdin` またはファイルからのページ分割された出力を表示します。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>。

- `stdin`の出力をページ分割して表示する:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- 1つ以上のファイルからページ分割された出力を表示する:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- タブを指定した数のスペースに変換する:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">スペース数</span>

- ページを表示する前に画面をクリアする:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /c`

- 5行目からの出力を表示する:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 拡張インタラクティブモードを有効にする(使い方はヘルプを参照):

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` /e`

- ヘルプを表示する:

`more /?`
