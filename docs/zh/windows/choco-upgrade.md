---
layout: page
title: windows/choco-upgrade (中文)
description: "使用 Chocolatey 升级一个或多个包。"
content_hash: 4e2c7fcc0a2f36f9b97c94fb8a21948bf3d7caca
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco upgrade

使用 Chocolatey 升级一个或多个包。
更多信息：<https://chocolatey.org/docs/commands-upgrade>.

- 升级一个或多个用空格分隔的软件包：

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名 包名 ..</span>

- 将一个包升级到指定版本：

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 升级全部包：

`choco upgrade all`

- 升级除指定的用逗号分隔的包之外的所有包：

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名 , 包名 ..</span>`"`

- 自动确认所有提示：

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --yes`

- 从自定义源处升级包：

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源 URL|别名</span>

- 提供一个用户名和密码来进行验证：

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
