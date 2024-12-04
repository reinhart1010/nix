---
layout: page
title: common/zcmp (中文)
description: "比较压缩文件。"
content_hash: c8eca4cdc0854f03f2874273720f9a8495d66a7e
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zcmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zcmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zcmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zcmp

比较压缩文件。
更多信息：<https://manned.org/zcmp>.

- 对两个通过 `gzip` 压缩的文件运行 `cmp` 命令：

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2.gz</span>

- 将一个文件与其 gzipped 版本进行比较（假设 `.gz` 已存在）：

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
