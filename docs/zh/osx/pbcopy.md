---
layout: page
title: osx/pbcopy (中文)
description: "将来自标准输入的数据放入剪贴板。"
content_hash: 73f28f22d67af5867f23aa821ce05d635d62cf9b
last_modified_at: 2023-06-13
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
---
# pbcopy

将来自标准输入的数据放入剪贴板。
相当于在键盘上按下 Cmd + C.
更多信息：<https://ss64.com/osx/pbcopy.html>.

- 将文件的内容放入剪贴板：

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将命令的执行结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`
