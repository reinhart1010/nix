---
layout: page
title: osx/launchctl (中文)
description: "用于启动守护程序（系统范围的服务）和启动代理程序（每个用户程序）的命令行界面，该界面指向苹果的`launchd` 管理工具。"
content_hash: e87c7cc776e6108ca8ba357654b3cc2251a9b11d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/launchctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/launchctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# launchctl

用于启动守护程序（系统范围的服务）和启动代理程序（每个用户程序）的命令行界面，该界面指向苹果的`launchd` 管理工具。
`launchd`加载放置在适当位置的基于 XML 的`*.plist`文件，并根据其定义的计划运行相应的命令。
更多信息：<https://manned.org/launchctl>.

- 每当用户登录时，自动将 plist 文件加载到 `launchd`：

`launchctl load ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的脚本</span>`.plist`

- 激活需要 root 权限才能运行和 / 或在任何用户登录时都应加载的脚本（注意路径中不能有`~`）：

`sudo launchctl load /Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root 脚本</span>`.plist`

- 激活一个系统范围的守护程序，以便在系统启动时加载（即使没有用户登录也会加载）：

`sudo launchctl load /Library/LaunchDaemons/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">系统脚本</span>`.plist`

- 显示所有加载的代理 / 守护进程，如果它们指定的进程当前正在运行，则显示 pid，如果停止那么返回了它们上次运行的时间和退出代码：

`launchctl list`

- 卸载当前加载的脚本，例如进行更改（注意：重新启动和 / 或登录后，plist 文件将自动加载到`launchd`）：

`launchctl unload ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的脚本</span>`.plist`

- 手动运行一个已知的（已加载的）脚本 / 守护进程，即使它不是正确的时间（注意：此命令使用脚本的标签，而不是文件名）：

`launchctl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的脚本</span>

- 手动终止与已知脚本 / 守护进程关联的进程（如果该进程正在运行）：

`launchctl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的脚本</span>
