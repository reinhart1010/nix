---
layout: page
title: linux/apt-mark (中文)
description: "修改已安装软件包状态的工具。"
content_hash: 592abc98b8d6f417e8f74686eec7f3a07eb1a37e
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
---
# apt-mark

修改已安装软件包状态的工具。
更多信息：<https://manpages.debian.org/latest/apt/apt-mark.8.html>.

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
