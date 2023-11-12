---
layout: page
title: windows/shutdown (中文)
description: "用于关闭，重新启动或注销计算机的工具。"
content_hash: 2acde6ce906f7e0ba857b69ef356ad081669fd4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/shutdown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

用于关闭，重新启动或注销计算机的工具。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- 关闭当前的计算机：

`shutdown /s`

- 重启当前的计算机：

`shutdown /r`

- 休眠当前的计算机：

`shutdown /h`

- 注销当前的计算机：

`shutdown /l`

- 指定在关闭之前等待的时间（以秒为单位）：

`shutdown /s /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒</span>

- 指定一个关机的理由：

`shutdown /s /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">理由</span>`"`

- 在超时之前取消关机指令：

`shutdown /a`

- 关闭远程的计算机：

`shutdown /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\ 主机名</span>
