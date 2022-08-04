---
layout: page
title: common/rubocop (中文)
description: "格式化 Ruby 文件。"
content_hash: 01209e16548ba55d233de1bb7a3e7f31b22daf4d
related_topics:
  - title: English version
    url: /en/common/rubocop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rubocop

格式化 Ruby 文件。
更多信息：<https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- 检查当前目录中的所有文件（包括子目录）：

`rubocop`

- 检查一个或多个指定文件或目录：

`rubocop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 / 文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 /</span>

- 将输出写入指定文件：

`rubocop --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录 / 文件名</span>

- 查看规则列表（格式化规则）：

`rubocop --show-cops`

- 排除格式规则：

`rubocop --except `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则 2</span>

- 只运行指定的规则：

`rubocop --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">规则 2</span>

- 自动更正文件（实验）：

`rubocop --auto-correct`
