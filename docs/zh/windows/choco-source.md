---
layout: page
title: windows/choco-source (中文)
description: "使用 Chocolatey 管理包的源。"
content_hash: 8bd0b5172045d9d8d8c4a09781f2ec368e1772b4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-source.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-source.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-source.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-source.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

使用 Chocolatey 管理包的源。
更多信息：<https://chocolatey.org/docs/commands-source>.

- 列出当前可用的源：

`choco source list`

- 添加一个新的包源：

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 添加包含凭据的新包源：

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 使用客户端证书添加新的包源：

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">证书的路径</span>

- 启用一个包源：

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 禁用一个包源：

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 移除一个包源：

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
