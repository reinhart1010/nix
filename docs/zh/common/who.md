---
layout: page
title: common/who (中文)
description: "显示当前登录用户和相关信息（进程，启动时间）。"
content_hash: ffca7012b0470c0b6251bdd3d1aa8b0fae82f4b4
last_modified_at: 2024-07-01
related_topics:
  - title: English version
    url: /en/common/who.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/who.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/who.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># who

显示当前登录用户和相关信息（进程，启动时间）。
更多信息：<https://www.gnu.org/software/coreutils/who>.

- 显示用户名，终端线路，和所有当前登录会话的时间：

`who`

- 仅显示当前终端会话信息：

`who am i`

- 显示所有可用信息：

`who -a`

- 显示所有可用信息，包含表格首部名称：

`who -a -H`
