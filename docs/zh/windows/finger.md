---
layout: page
title: windows/finger (中文)
description: "返回有关指定系统上的一个或多个用户的信息。"
content_hash: ede6cb4f896e3ef9a32901938944900845c59cde
related_topics:
  - title: English version
    url: /en/windows/finger.html
    icon: bi bi-globe
---
# finger

返回有关指定系统上的一个或多个用户的信息。
远程系统必须运行 Finger 服务。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- 显示有关特定用户的信息：

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 在指定的主机上显示所有用户的信息：

`finger @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>

- 以更长的格式显示信息：

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` -l`

- 显示帮助信息：

`finger /?`
