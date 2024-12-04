---
layout: page
title: common/zipinfo (中文)
description: "列出 Zip 文件内容的详细信息。"
content_hash: 367b6c2f4b13d0ed758bf7cd1554478b8c1240b7
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zipinfo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zipinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipinfo

列出 Zip 文件内容的详细信息。
更多信息：<https://manned.org/zipinfo>.

- 以长格式（权限、所有权、大小和修改日期）列出 Zip 文件中的所有文件：

`zipinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.zip</span>

- 列出 Zip 文件中的所有文件：

`zipinfo -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.zip</span>
