---
layout: page
title: osx/rubocop (中文)
description: "格式化 Ruby 文件。"
content_hash: 73a904e0f81551bc0157fa609e57e8974529def2
related_topics:
  - title: English version
    url: /en/osx/rubocop.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/rubocop.html
    icon: bi bi-globe
---
# rubocop

格式化 Ruby 文件。

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
