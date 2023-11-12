---
layout: page
title: windows/del (中文)
description: "删除一个或多个文件。"
content_hash: 33941317bf88d9ce8c93cd6d9a768c8c85a2f843
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

删除一个或多个文件。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 删除一个或多个以空格分隔的文件：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 文件 ..</span>

- 在删除每个文件之前提示确认：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` /p`

- 强制删除只读文件：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` /f`

- 递归删除所有子目录中的文件：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` /s`

- 在基于全局通配符删除文件时不提示确认：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` /q`

- 显示帮助和所有的属性列表：

`del /?`

- 根据指定的属性删除文件：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">属性</span>
