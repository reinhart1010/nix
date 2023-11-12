---
layout: page
title: windows/xcopy (中文)
description: "复制文件和目录树。"
content_hash: aea3686428bf1f65234eafdc42909445cfdedf4c
last_modified_at: 2023-11-12
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
  - title: polski version
    url: /pl/windows/xcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcopy

复制文件和目录树。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- 复制文件到指定的路径：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">被复制的目录路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>

- 列出在复制前将要被复制的文件：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /p`

- 仅复制目录结构，不包括文件：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /t`

- 复制时包含空目录：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /e`

- 复制文件时保留 ACL 信息：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /o`

- 网络连接丢失时允许恢复：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /z`

- 当文件存在于目标路径中时禁用提示：

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标路径</span>` /y`

- 显示详细的使用帮助：

`xcopy /?`
