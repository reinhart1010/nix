---
layout: page
title: common/zdiff (中文)
description: "对 `gzip` 压缩文件调用 `diff`。"
content_hash: 1ae4272b56a14ed99f403905fb7763e186d88b49
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zdiff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zdiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zdiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zdiff

对 `gzip` 压缩文件调用 `diff`。
更多信息：<https://manned.org/zdiff>.

- 比较两个文件，必要时解压它们：

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件2.gz</span>

- 将文件与同名的 `gzip` 压缩文件进行比较：

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
