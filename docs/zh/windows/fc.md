---
layout: page
title: windows/fc (中文)
description: "比较两个文件或文件集之间的差异。"
content_hash: 0a37a61812d10472478c185f992d2e1b48232426
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/fc.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

比较两个文件或文件集之间的差异。
使用通配符（*）来比较文件集。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- 比较两个指定的文件：

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 比较时不区分大小写：

`fc /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 将文件作为 Unicode 文本来进行比较：

`fc /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 将文件作为 ASCII 文本来进行比较：

`fc /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 将文件作为二进制来比较：

`fc /b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 禁用制表符到空格的扩展：

`fc /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 压缩空格（制表符和空格）进行比较：

`fc /w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>
