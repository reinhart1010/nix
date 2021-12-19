---
layout: page
title: windows/clip (中文)
description: "将输入的内容复制到 Windows 的剪贴板。"
content_hash: 12000945271e17b03f6aac7b4ea5e5279386c664
related_topics:
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/clip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clip

将输入的内容复制到 Windows 的剪贴板。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/clip>.

- 用管道将命令的输出内容复制到 Windows 剪贴板：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- 将一个文件中的内容复制到 Windows 剪贴板：

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>
