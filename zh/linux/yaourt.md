---
layout: page
title: linux/yaourt (中文)
description: "Arch Linux 中用于从 Arch User Repository 中构建软件包的工具。"
content_hash: a96117977d67db9db4f3732b1be32397ba3af7f3
related_topics:
  - title: English version
    url: /en/linux/yaourt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yaourt.html
    icon: bi bi-globe
---
# yaourt

Arch Linux 中用于从 Arch User Repository 中构建软件包的工具。
更多信息：<https://linuxcommandlibrary.com/man/yaourt>.

- 同步并更新所有软件包（包括 AUR）：

`yaourt -Syua`

- 安装一个新的软件包（包括 AUR）：

`yaourt -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除一个软件包和它的依赖（包括 AUR 软件包）：

`yaourt -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 在软件包数据库中搜索一个关键字（包括 AUR）：

`yaourt -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 列出已安装的软件包、版本和仓库（AUR 软件包将被列在 'local' 仓库下）：

`yaourt -Q`
