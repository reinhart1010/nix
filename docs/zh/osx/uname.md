---
layout: page
title: osx/uname (中文)
description: "打印当前计算机及其上运行的操作系统的详细信息。"
content_hash: d43390635df32c8852c93a51d01b82b0a2889461
related_topics:
  - title: English version
    url: /en/osx/uname.html
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

- 打印硬件相关：架构信息和处理器：

`uname -mp`

- 打印软件相关信息：操作系统、版本号和版本：

`uname -srv`

- 打印系统的节点名称（主机名）：

`uname -n`

- 打印所有可用的系统信息（硬件、软件、节点名）：

`uname -a`
