---
layout: page
title: common/yank (中文)
description: "从 stdin 读取输入并显示一个选择界面，该界面允许选择一个字段并将其复制到剪贴板。"
content_hash: f1ac04b396cf39be08a29d9fd34dec6575638b2c
related_topics:
  - title: English version
    url: /en/common/yank.html
    icon: bi bi-globe
---
# yank

从 stdin 读取输入并显示一个选择界面，该界面允许选择一个字段并将其复制到剪贴板。
更多信息：<https://manned.org/yank>.

- 使用默认分隔符（\f, \n, \r, \s, \t）：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank`

- 输入单行：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sudo dmesg</span>` | yank -l`

- 使用特定分 `=` 隔符输入：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo hello=world</span>` | yank -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">=</span>

- 只有与特定正则表达式匹配的内容才输入：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps ux</span>` | yank -g "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[0-9]+</span>`"`
