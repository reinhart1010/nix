---
layout: page
title: windows/find (中文)
description: "在一个或多个文件里查找指定字符串。"
content_hash: fcbbd59c7164a504cd36f3b534f71e708478fd7c
related_topics:
  - title: English version
    url: /en/windows/find.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/find.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/find.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/find.html
    icon: bi bi-globe
---
# find

在一个或多个文件里查找指定字符串。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- 查找包含指定字符串的行：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>

- 查找不包含指定字符串的行：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` /v`

- 显示包含指定字符串的行的总数：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` /c`

- 显示匹配的行的行数：

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` /n`
