---
layout: page
title: common/quilt (中文)
description: "管理一系列的补丁。"
content_hash: 091ea8556cf8e8a115522800bb6df3855fa55396
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/quilt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/quilt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/quilt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quilt

管理一系列的补丁。
更多信息：<https://savannah.nongnu.org/projects/quilt>.

- 从文件中导入一个已有补丁：

`quilt import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件名.patch</span>

- 创建一个新补丁：

`quilt new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.patch</span>

- 将文件添加到当前补丁：

`quilt add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 编辑文件后，用更改刷新当前补丁：

`quilt refresh`

- 应用系列文件中的所有补丁：

`quilt push -a`

- 移除所有已应用的补丁：

`quilt pop -a`
