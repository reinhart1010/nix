---
layout: page
title: common/uname (中文)
description: "输出关于当前机器和运行在该机器上的操作系统的详细信息。"
content_hash: 01b975e726bbea1c26e044d14581937ac0d015bf
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/uname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/uname.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/uname.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uname

输出关于当前机器和运行在该机器上的操作系统的详细信息。
注意：如需了解操作系统的其他信息，请尝试使用 `lsb_release` 命令。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html>.

- 打印硬件相关信息：机器和处理器：

`uname -mp`

- 打印软件相关信息：操作系统、发行号和版本：

`uname -srv`

- 打印系统的名称（主机名）：

`uname -n`

- 打印所有可用的系统信息（硬件、软件、名称）：

`uname -a`
