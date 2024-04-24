---
layout: page
title: linux/readelf (中文)
description: "显示 EFI 文件信息。"
content_hash: de6371bcbc76964f65be72cc06a20fdf2ee47b2d
last_modified_at: 2024-04-24
related_topics:
  - title: English version
    url: /en/linux/readelf.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># readelf

显示 EFI 文件信息。
更多信息：<http://man7.org/linux/man-pages/man1/readelf.1.html>.

- 显示 ELF 所有文件信息：

`readelf -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- 显示 ELF 文件的所有头信息：

`readelf --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- 如果存在符号表项，则显示 ELF 文件内的符号表项：

`readelf --symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>

- 显示 ELF 文件头信息：

`readelf --file-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>
