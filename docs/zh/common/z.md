---
layout: page
title: common/z (中文)
description: "记录被使用次数最多的目录并允许在它们之间以字符串或正则表达式来进行匹配和跳转。"
content_hash: 1e1920df03ebb978aa834a93deec2f614730b3ae
related_topics:
  - title: English version
    url: /en/common/z.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/z.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/z.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/z.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># z

记录被使用次数最多的目录并允许在它们之间以字符串或正则表达式来进行匹配和跳转。
更多信息：<https://github.com/rupa/z>.

- 跳转到一个名字带有 "foo" 的文件夹：

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 跳转到一个名字带有 "foo" 并且后面带有 "bar" 的文件夹（例：`fooesbar`）：

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 跳转到名字带有 "foo" 并且拥有最高访问次数的文件夹：

`z -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 跳转到最近使用的名字带有 "foo" 的文件夹：

`z -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 列出在 `z` 的数据库中名字带有 "foo" 的文件夹：

`z -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 将当前文件夹从 `z`的数据库中移除：

`z -x .`
