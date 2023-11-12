---
layout: page
title: windows/choco-list (中文)
description: "使用 Chocolatey 显示包列表。"
content_hash: 33b612097803e35814760289187af3154ce9dfc7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

使用 Chocolatey 显示包列表。
更多信息：<https://chocolatey.org/docs/commands-list>.

- 列出所有可用的包：

`choco list`

- 列出所有本地已安装的包：

`choco list --local-only`

- 显示包含本地程序的列表：

`choco list --include-programs`

- 只显示已批准的包：

`choco list --approved-only`

- Specify a custom source to display packages from 指定一个源来显示包列表：

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源 URL|别名</span>

- 提供一个用户名和密码来进行验证：

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
