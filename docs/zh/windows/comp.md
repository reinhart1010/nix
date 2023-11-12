---
layout: page
title: windows/comp (中文)
description: "比较两个文件或文件集的内容。"
content_hash: b2170ffb4e25281f2c08059ca7852397fb8b5ea8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/comp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/comp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comp

比较两个文件或文件集的内容。
使用通配符（*）来比较文件集。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- 交互式比较文件：

`comp`

- 比较两个指定的文件：

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 比较两个文件集：

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 1/*</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 2/*</span>

- 以十进制格式显示差异：

`comp /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 以 ASCII 字符显示差异：

`comp /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 显示不同的行数：

`comp /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 比较文件时不区分大小写：

`comp /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>

- 只比较每个文件前 5 行的内容：

`comp /n=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 1 的路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 2 的路径</span>
