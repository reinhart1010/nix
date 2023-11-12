---
layout: page
title: windows/clip (中文)
description: "将输入的内容复制到 Windows 的剪贴板。"
content_hash: 77497641c95a594e64c352f233518f9353c25633
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
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/clip.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clip

将输入的内容复制到 Windows 的剪贴板。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- 用管道将命令的输出内容复制到 Windows 剪贴板：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- 将一个文件中的内容复制到 Windows 剪贴板：

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>
