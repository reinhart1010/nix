---
layout: page
title: osx/osascript (中文)
description: "在命令行中运行指定的 AppleScript 或 JavaScript 脚本程序。"
content_hash: 2054f773adfd9ca0105bbbbdde47253ac928358d
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/osascript.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/osascript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/osascript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# osascript

在命令行中运行指定的 AppleScript 或 JavaScript 脚本程序。
更多信息：<https://keith.github.io/xcode-man-pages/osascript.1.html>.

- 运行一个 AppleScript 命令：

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say '你好世界'</span>`"`

- 运行多条 AppleScript 命令：

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say '你好'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say '世界'</span>`"`

- 运行一个已编译的脚本（`*.scpt`），包脚本（`*.scptd`），或明文的（`*.applescript`）AppleScript 文件：

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 / 脚本文件.scpt</span>

- 获取应用程序的包名（这个包名，可以用在命令 `open -b` 中）：

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序名</span>`"'`

- 运行一个 JavaScript 命令：

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('你好世界！');</span>`"`

- 运行 JavaScript 文件：

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 文件名.js</span>
