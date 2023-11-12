---
layout: page
title: windows/doskey (中文)
description: "管理宏，Windows 命令和命令行。"
content_hash: a0ca5856f59668c2c9c1fa46801d69dcad5d25e4
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/doskey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/doskey.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/doskey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/doskey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doskey

管理宏，Windows 命令和命令行。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- 列出可用的宏：

`doskey /macros`

- 创建一个新的宏：

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宏的名称</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>`"`

- 为指定可执行文件创建新的宏：

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宏的名称</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>`"`

- 删除一个宏：

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宏的名称</span>` =`

- 列出所有储存在内存中的命令：

`doskey /history`

- 将宏保存到文件以便于移植：

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">保存宏的文件名</span>

- 从文件中加载宏：

`doskey /macrofile = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">保存宏的文件名</span>
