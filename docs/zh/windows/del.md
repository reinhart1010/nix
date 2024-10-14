---
layout: page
title: windows/del (中文)
description: "删除一个或多个文件。"
content_hash: 27cb7dad2966cca6b48de4e15f1f5a06fe5db900
last_modified_at: 2024-10-14
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
tldri18n_status: 2
---
# del

删除一个或多个文件。
在 PowerShell 中，此命令为 `Remove-Item` 的別名。本页的描述是基于命令提示符 (`cmd`) 中的 `del`。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 查阅 PowerShell 的对应命令:

`tldr remove-item`

- 删除一个或多个文件 (可使用通配符)：

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件1 文件2 ...</span>

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
