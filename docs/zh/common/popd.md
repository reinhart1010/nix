---
layout: page
title: common/popd (中文)
description: "通过 pushd shell 内置程序删除目录堆栈中的目录。"
content_hash: b565fb0006158690fa1d721e60c75399f5d92321
last_modified_at: 2023-11-12
related_topics:
  - title: dansk version
    url: /da/common/popd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/popd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># popd

通过 pushd shell 内置程序删除目录堆栈中的目录。
更多信息：<https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- 从堆栈中删除顶部目录，并用 `cd` 跳转到该目录：

`popd`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd +N`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表右侧开始）：

`popd -N`
