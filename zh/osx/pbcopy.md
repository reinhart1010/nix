---
layout: page
title: osx/pbcopy (中文)
description: "将标准输出放入剪贴板（命令行里的 cmd + C）。"
content_hash: 15ab8f67e08f78b8430d65fad159a92821e73991
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
---
# pbcopy

将标准输出放入剪贴板（命令行里的 cmd + C）。

- 将文件的内容放入剪贴板：

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 将命令的执行结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`
