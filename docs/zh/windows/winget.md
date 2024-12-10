---
layout: page
title: windows/winget (中文)
description: "Windows 软件包管理器命令行工具。"
content_hash: aafbd8b2da598787c9ab7c8e9609fd5db2ea2645
last_modified_at: 2024-12-10
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># winget

Windows 软件包管理器命令行工具。
更多信息：<https://learn.microsoft.com/windows/package-manager/winget>.

- 安装一个包：

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 移除一个包（注意：`remove` 也可以用来代替 `uninstall`）：

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 显示一个包的信息：

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 搜索一个包：

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 将所有包升级到最新版本：

`winget upgrade --all`

- 列出所有可以通过 `winget` 管理的已安装包：

`winget list --source winget`

- 从文件导入包，或将已安装的包导出到文件：

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 在提交合并到 winget-pkgs 仓库之前验证清单：

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/清单</span>
