---
layout: page
title: common/unlink (中文)
description: "从文件系统中删除对文件的链接。"
content_hash: a5ffaa38d7a02f46a6283a7c938dc6ae26cfac85
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/unlink.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unlink.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unlink.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unlink.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unlink

从文件系统中删除对文件的链接。
如果链接是文件的最后一个，文件内容将丢失。
更多信息：<https://www.gnu.org/software/coreutils/unlink>.

- 如果是最后一个链接，则删除指定的文件：

`unlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
