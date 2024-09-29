---
layout: page
title: linux/mac2unix (中文)
description: "将 macOS 样式的行尾更改为 Unix 样式。"
content_hash: 658de9c81dc55e13611840cf600e8ae1f8152198
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/linux/mac2unix.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mac2unix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mac2unix

将 macOS 样式的行尾更改为 Unix 样式。
用 LF 替换 CR.
更多信息：<https://manned.org/mac2unix>.

- 更改文件的行尾：

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 使用 Unix 样式的行尾创建副本：

`mac2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新文件名</span>
