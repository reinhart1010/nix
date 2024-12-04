---
layout: page
title: common/zrun (中文)
description: "透明地将压缩的参数文件解压缩并传递给某个命令。"
content_hash: 81346e29df3de09f05e3b7c0694cfcf6c7f831ac
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zrun.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zrun.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zrun.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zrun

透明地将压缩的参数文件解压缩并传递给某个命令。
更多信息：<https://joeyh.name/code/moreutils/>.

- 使用解压后的压缩参数文件运行指定命令：

`zrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件1.gz 路径/到/文件2.bz2 ...</span>
