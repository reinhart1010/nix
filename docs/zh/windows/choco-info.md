---
layout: page
title: windows/choco-info (中文)
description: "显示有关 Chocolatey 包的详细信息。"
content_hash: 87232e4e471b92b730834878d06c1334178e0ebd
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-info.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-info.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-info.html
    icon: bi bi-globe
---
# choco info

显示有关 Chocolatey 包的详细信息。
更多信息：<https://chocolatey.org/docs/commands-info>.

- 显示指定包的信息：

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 显示一个本地已安装包的信息：

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --local-only`

- 从一个自定义的源来获取包的信息：

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源 URL|别名</span>

- 提供一个用户名和密码来进行验证：

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
