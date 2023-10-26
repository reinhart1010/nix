---
layout: page
title: common/powershell (中文)
description: "专为系统管理而设计的命令行 shell 和脚本语言。"
content_hash: a245dbedbcdba0e937887453d3d5e4c3cd44a076
last_modified_at: 2023-10-26
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/powershell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
