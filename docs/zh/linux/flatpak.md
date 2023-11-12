---
layout: page
title: linux/flatpak (中文)
description: "构建、安装和运行 Flatpak 应用和运行时。"
content_hash: 247903f34c361848466448a35448ce79e7dd55c8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

构建、安装和运行 Flatpak 应用和运行时。
更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- 运行已安装应用：

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>

- 从远程源安装应用：

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程源名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>

- 列出所有应用和运行时：

`flatpak list`

- 更新所有已安装的应用和运行时：

`flatpak update`

- 添加远程源：

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程源名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程源网址</span>

- 列出所有已配置的远程源：

`flatpak remote-list`

- 移除一个已安装的应用程序：

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>

- 显示一个已安装的应用程序的信息：

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>
