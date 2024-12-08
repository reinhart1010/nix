---
layout: page
title: common/fd (中文)
description: "`find` 的替代工具。"
content_hash: 0984c4f994f0a416c6330ab0c46bc3b35a7155ef
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/fd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fd

`find` 的替代工具。
旨在比 `find` 更快且更易于使用。
更多信息：<https://github.com/sharkdp/fd>.

- 递归查找当前目录中匹配特定模式的文件：

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串|正则表达式</span>`"`

- 查找以特定字符串开头的文件：

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^字符串</span>`"`

- 查找具有特定扩展名的文件：

`fd --extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- 在特定目录中查找文件：

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串|正则表达式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 在搜索中包含被忽略和隐藏的文件：

`fd --hidden --no-ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串|正则表达式</span>`"`

- 对每个返回的搜索结果执行命令：

`fd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串|正则表达式</span>`" --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>
