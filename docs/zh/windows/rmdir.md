---
layout: page
title: windows/rmdir (中文)
description: "删除目录及其内容。"
content_hash: a6d96421baa73f532024f99c95218b8742623798
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rmdir

删除目录及其内容。
在 PowerShell 中，此命令是 `Remove-Item` 的别名。此文档基于 `cmd` 版本的 `rmdir`。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 查看等效的 PowerShell 命令的文档：

`tldr remove-item`

- 删除一个空目录：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径\到\目录</span>

- 递归删除目录及其内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径\到\目录</span>` /s`

- 递归删除目录及其内容，无需提示：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径\到\目录</span>` /s /q`
