---
layout: page
title: linux/unix2dos (中文)
description: "将 Unix 样式的行尾更改为 DOS 样式。"
content_hash: 664cdc1ae0e353867e7be896673afe12b30424e4
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/linux/unix2dos.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unix2dos

将 Unix 样式的行尾更改为 DOS 样式。
用 CRLF 替换 LF.
更多信息：<https://manned.org/unix2dos>.

- 更改文件的行尾：

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 使用 DOS 样式的行尾创建副本：

`unix2dos -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新文件名</span>
