---
layout: page
title: common/export (中文)
description: "命令为当前 shell 中的子进程进行环境变量设置。"
content_hash: eae310f02f773d826824dab792feb6e617f7633f
related_topics:
  - title: Deutsch version
    url: /de/common/export.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/export.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/export.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># export

命令为当前 shell 中的子进程进行环境变量设置。
更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- 设置为新的环境变量：

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">某变量名</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 删除环境变量：

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">某变量名</span>

- 给 PATH 追加新的路径进去：

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">追加的 path 路径</span>
