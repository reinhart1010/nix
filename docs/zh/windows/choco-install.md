---
layout: page
title: windows/choco-install (中文)
description: "使用 Chocolatey 下载一个或多个包。"
content_hash: c521c9a620c05e3611e6a04c62bb8a2c69ac09e4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/choco-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-install.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco install

使用 Chocolatey 下载一个或多个包。
更多信息：<https://chocolatey.org/docs/commands-install>.

- 安装一个或多个用空格分隔的软件包：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名 包名 ..</span>

- 从一个自定义的配置文件中安装包：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>

- 安装一个特定的 "nuspec" 或 "nupkg" 文件：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 安装一个指定版本的包：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 允许安装一个包的多个版本：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --allow-multiple`

- 自动确认所有提示：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --yes`

- 从自定义的源处获取包：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源 URL|别名</span>

- 提供一个用户名和密码来进行验证：

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
