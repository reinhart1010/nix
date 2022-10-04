---
layout: page
title: windows/powershell (中文)
description: "专为系统管理而设计的命令行 shell 和脚本语言。"
content_hash: a245dbedbcdba0e937887453d3d5e4c3cd44a076
related_topics:
  - title: français version
    url: /fr/windows/powershell.html
    icon: bi bi-globe
---
# powershell

专为系统管理而设计的命令行 shell 和脚本语言。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- 在命令提示符窗口中启动 Windows PowerShell 会话：

`powershell`

- 加载一个特定的 PowerShell 控制台文件：

`powershell -PSConsoleFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/file</span>

- 用指定版本的 PowerShell 启动会话：

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 防止运行启动命令后 shell 退出：

`powershell -NoExit`

- 描述发送到 PowerShell 的数据格式：

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- 设定 PowerShell 输出的格式：

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- 显示帮助：

`powershell -Help`
