---
layout: page
title: linux/unix2mac (中文)
description: "将 Unix 样式的行尾更改为 macOS 样式。"
content_hash: 06600f7b8eefc25e7b8a492e3f90026588ec79a4
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/linux/unix2mac.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2mac.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unix2mac

将 Unix 样式的行尾更改为 macOS 样式。
用 CR 替换 LF.
更多信息：<https://manned.org/unix2mac>.

- 更改文件的行尾：

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 使用 macOS 样式的行尾创建副本：

`unix2mac -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新文件名</span>
