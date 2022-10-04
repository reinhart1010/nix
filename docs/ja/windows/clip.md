---
layout: page
title: windows/clip (日本語)
description: "入力コンテンツをWindowsクリップボードにコピーします。"
content_hash: b89e3e70ab5bb17dfabd4d374694f4453b360f18
related_topics:
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
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
