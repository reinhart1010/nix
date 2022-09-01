---
layout: page
title: common/command (中文)
description: "Command 强制当前 shell 执行指定程序，并忽略具有相同名称的任何函数、内置函数和别名。"
content_hash: aed82e2a845e35999c309463674597f1255126b5
related_topics:
  - title: English version
    url: /en/common/command.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/command.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/command.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/command.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/command.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/command.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># command

Command 强制当前 shell 执行指定程序，并忽略具有相同名称的任何函数、内置函数和别名。
更多信息：<https://manned.org/command>.

- 从字面上执行 `ls` 程序，即使存在 `ls` 别名：

`command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- 显示指定命令的可执行程序路径或别名定义：

`command -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令名</span>
