---
layout: page
title: linux/apt-mark (中文)
description: "修改已安装软件包状态的工具。"
content_hash: 1af9fc2038f5d81b6106745986008705d0889cb6
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

修改已安装软件包状态的工具。
更多信息：<https://manned.org/apt-mark.8>.

- 将一个软件包标记为自动安装：

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包名</span>

- 将一个软件包保持在当前版本，防止对其更新：

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包名</span>

- 允许对一个软件包更新：

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包名</span>

- 列出手动安装的软件包：

`apt-mark showmanual`

- 列出保持当前版本而不更新的软件包：

`apt-mark showhold`
