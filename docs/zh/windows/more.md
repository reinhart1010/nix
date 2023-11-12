---
layout: page
title: windows/more (中文)
description: "分页显示标准输入或文件的输出。"
content_hash: 1d6960e1f948387bf69f5f7a62fd8c6417ca9455
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/more.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

分页显示标准输入或文件的输出。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- 分页显示标准输入的输出：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- 分页显示一个或多个文件的内容：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 将制表符转换为指定的空格数：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">空格数</span>

- 显示内容前先清屏：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` /c`

- 从第 5 行开始显示输出：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 启用扩展交互模式（请参阅使用帮助）：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` /e`

- 显示全部帮助信息：

`more /?`
