---
layout: page
title: windows/rmdir (中文)
description: "删除一个目录和其中的内容。"
content_hash: 86f141a2d963bce0544146a0c2760435fedd97e2
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
---
# rmdir

删除一个目录和其中的内容。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 删除一个空目录：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 递归删除一个目录及其中的内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>` /s`

- 在没有提示的情况下递归删除目录及其内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` /s /q`
