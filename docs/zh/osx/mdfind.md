---
layout: page
title: osx/mdfind (中文)
description: "列出与给定查询匹配的文件。"
content_hash: 2fe59a1a754742bd12443dd93b7e6954e8bb052a
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/mdfind.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mdfind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdfind

列出与给定查询匹配的文件。
更多信息：<https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- 按文件名查找文件：

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 按内容查找文件：

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查找的字符串</span>`"`

- 在给定目录中查找包含字符串的文件：

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>`"`
