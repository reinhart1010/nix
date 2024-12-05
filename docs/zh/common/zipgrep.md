---
layout: page
title: common/zipgrep (中文)
description: "在 Zip 压缩档案中的文件中使用扩展正则表达式查找模式（支持 `?`、`+`、`{}`、`()` 和 `|`）。"
content_hash: 609be3dbf31f19d5e952635123b4e6d725e0e2de
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zipgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zipgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipgrep

在 Zip 压缩档案中的文件中使用扩展正则表达式查找模式（支持 `?`、`+`、`{}`、`()` 和 `|`）。
更多信息：<https://manned.org/zipgrep>.

- 在 Zip 压缩档案中搜索一个模式：

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 打印匹配的文件名和行号：

`zipgrep -H -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 搜索与模式不匹配的行：

`zipgrep -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 指定在 Zip 压缩档案中要搜索的文件：

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">要搜索的文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">要搜索的文件2</span>

- 排除在 Zip 压缩档案中要搜索的文件：

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索模式</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">要排除的文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">要排除的文件2</span>
