---
layout: page
title: common/powershell (中文)
description: "专为系统管理而设计的命令行 shell 和脚本语言。"
content_hash: a245dbedbcdba0e937887453d3d5e4c3cd44a076
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/powershell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/powershell.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/powershell.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># powershell

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
