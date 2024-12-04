---
layout: page
title: common/zcat (中文)
description: "打印 `gzip` 压缩文件中的数据。"
content_hash: 7f6409f92501b57d29f13d52aa1030f71f398657
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zcat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zcat

打印 `gzip` 压缩文件中的数据。
更多信息：<https://www.gnu.org/software/gzip/manual/gzip.html>.

- 将 `gzip` 压缩档案的解压缩内容打印到 `stdout`：

`zcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.txt.gz</span>

- 将 `gzip` 压缩档案的压缩详细信息打印到 `stdout`：

`zcat -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.txt.gz</span>
