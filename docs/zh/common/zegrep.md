---
layout: page
title: common/zegrep (中文)
description: "使用 `egrep` 在压缩文件中查找扩展正则表达式模式。"
content_hash: c7918e54ee362b6930175a792932b8cbb097fbe0
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zegrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zegrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zegrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zegrep

使用 `egrep` 在压缩文件中查找扩展正则表达式模式。
更多信息：<https://www.unix.com/man-page/freebsd/1/zegrep/>.

- 在压缩文件中搜索扩展正则表达式（支持 `?`, `+`, `{}`, `()` 和 `|`），区分大小写：

`zegrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 在压缩文件中搜索扩展正则表达式（支持 `?`, `+`, `{}`, `()` 和 `|`），忽略大小写：

`zegrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 搜索不匹配模式的行：

`zegrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 打印每个匹配项的文件名和行号：

`zegrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 搜索匹配模式的行，仅打印匹配的文本：

`zegrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 在压缩文件中递归搜索文件中的模式：

`zegrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
