---
layout: page
title: osx/uname (中文)
description: "打印当前计算机及其上运行的操作系统的详细信息。"
content_hash: 48c192cb96d998c0447778ab8fcdc65bf70590cd
related_topics:
  - title: English version
    url: /en/osx/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/osx/uname.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

打印当前计算机及其上运行的操作系统的详细信息。
注意：有关操作系统的其他信息，请尝试使用 `sw-vers` 命令。
更多信息：<https://ss64.com/osx/uname.html>.

- 打印内核名称：

`uname`

- 打印系统架构和处理器信息：

`uname -mp`

- 打印内核名称、内核版本号和内核版本详细信息：

`uname -srv`

- 打印系统主机名：

`uname -n`

- 打印所有可用的系统信息：

`uname -a`
