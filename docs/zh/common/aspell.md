---
layout: page
title: common/aspell (中文)
description: "交互式拼写检查工具。"
content_hash: 66daa95afb2bb844ac85f66d0fbe939aa44017a4
last_modified_at: 2024-08-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

交互式拼写检查工具。
更多信息：<http://aspell.net/>.

- 为一个文件做拼写检查：

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 列出来自标准输入的拼写错误单词：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` | aspell list`

- 列出可用的字典语言：

`aspell dicts`

- 指定不同的语言（取 ISO 639 语言代码的 2 个字母）来运行 `aspell`：

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- 列出来自标准输入的拼写错误单词，并且忽略个人单词列表中的单词：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">个人单词列表.pws</span>` list`
