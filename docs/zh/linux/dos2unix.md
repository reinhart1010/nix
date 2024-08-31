---
layout: page
title: linux/dos2unix (中文)
description: "将 DOS 样式的行尾更改为 Unix 样式。"
content_hash: 87fcfe8490ad7a0ffa5ea3ebbaf45b59dc31b652
last_modified_at: 2024-08-31
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dos2unix

将 DOS 样式的行尾更改为 Unix 样式。
用 LF 替换 CRLF.
更多信息：<https://manned.org/dos2unix>.

- 更改文件的行尾：

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 使用 Unix 样式的行尾创建副本：

`dos2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>
