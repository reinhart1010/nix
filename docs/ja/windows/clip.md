---
layout: page
title: windows/clip (日本語)
description: "入力コンテンツをWindowsクリップボードにコピーします。"
content_hash: b89e3e70ab5bb17dfabd4d374694f4453b360f18
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/clip.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/clip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clip

入力コンテンツをWindowsクリップボードにコピーします。
詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>

- コマンドライン出力をWindowsクリップボードにパイプします:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- ファイルの内容をWindowsクリップボードにコピーします:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>

- 末尾に改行が付いたテキストをWindowsクリップボードにコピーします:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">テキスト</span>` | clip`

- 末尾の改行なしでテキストをWindowsクリップボードにコピーします:

`echo | set /p="テキスト" | clip`
