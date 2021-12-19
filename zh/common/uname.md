---
layout: page
title: common/uname (中文)
description: "输出关于当前机器和运行在该机器上的操作系统的详细信息。"
content_hash: 2373188d1b59752ba8bfbc9bb2d3a25222898269
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/uname.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/uname.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

输出关于当前机器和运行在该机器上的操作系统的详细信息。
注意：如需了解操作系统的其他信息，请尝试使用 `lsb_release` 命令。
更多信息：<https://www.gnu.org/software/coreutils/uname>.

- 打印硬件相关信息：机器和处理器：

`uname -mp`

- 打印软件相关信息：操作系统、发行号和版本：

`uname -srv`

- 打印系统的名称（主机名）：

`uname -n`

- 打印所有可用的系统信息（硬件、软件、名称）：

`uname -a`
