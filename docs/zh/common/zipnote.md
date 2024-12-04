---
layout: page
title: common/zipnote (中文)
description: "查看、添加或编辑 Zip 压缩包的注释。"
content_hash: 955ec5e4719926c852fc068aaab428b2e954dc2d
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zipnote.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zipnote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipnote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipnote

查看、添加或编辑 Zip 压缩包的注释。
文件在 Zip 压缩包中也可以被重命名。
更多信息：<https://manned.org/zipnote>.

- 查看 Zip 压缩包中的注释：

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 将 Zip 压缩包中的注释提取到一个文件：

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.txt</span>

- 从一个文件中添加/更新 Zip 压缩包中的注释：

`zipnote -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.txt</span>
