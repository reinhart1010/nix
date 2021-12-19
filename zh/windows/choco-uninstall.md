---
layout: page
title: windows/choco-uninstall (中文)
description: "使用 Chocolatey 卸载一个或多个包。"
content_hash: 0b5651c1a0160ae510d74d7b250b66dfec72cd3b
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
---
# choco uninstall

使用 Chocolatey 卸载一个或多个包。
更多信息：<https://chocolatey.org/docs/commands-uninstall>.

- 卸载一个或多个用空格分隔的软件包：

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名 『包名』 ..</span>

- 卸载一个指定版本的包：

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 自动确认所有提示：

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --yes`

- 卸载时同时删除其所有的依赖：

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --remove-dependencies`

- 卸载全部包：

`choco uninstall all`
