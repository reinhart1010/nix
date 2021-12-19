---
layout: page
title: windows/choco-pin (中文)
description: "使用 Chocolatey 将一个包固定到指定的版本。"
content_hash: 03b1d55b68aa08499b7bf29311ff7e12f059e8c7
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-pin.html
    icon: bi bi-globe
---
# choco pin

使用 Chocolatey 将一个包固定到指定的版本。
被固定版本的包会在更新时自动忽略。
更多信息：<https://chocolatey.org/docs/commands-pin>.

- 显示被固定的包以及他们对应的版本号：

`choco pin list`

- 将一个包固定至当前版本：

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 将一个包固定直指定的版本：

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 移除指定包的固定状态：

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>
