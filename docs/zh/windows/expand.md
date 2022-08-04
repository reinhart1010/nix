---
layout: page
title: windows/expand (中文)
description: "解压一个或多个 cab 文件。"
content_hash: 2f326529f7eaabd859f726407d1d4112d8f137b4
related_topics:
  - title: English version
    url: /en/windows/expand.html
    icon: bi bi-globe
---
# expand

解压一个或多个 cab 文件。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/expand>.

- 将单文件 cab 文件解压到指定目录：

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cab 文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>

- 列出 cab 文件中的所有文件：

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cab 文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>` -d`

- 从 cab 文件中解压所有的文件：

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cab 文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>` -f:*`

- 从 cab 文件中解压一个特定的文件：

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cab 文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>` -f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 解压缩时忽略目录结构，并将它们添加到单个目录中：

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cab 文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定的目录</span>` -i`
