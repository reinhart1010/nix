---
layout: page
title: osx/pbcopy (中文)
description: "将来自标准输入的数据放入剪贴板。"
content_hash: df500c3785a2bc197fff6e766898af27669485b5
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbcopy

将来自标准输入的数据放入剪贴板。
相当于在键盘上按下 Cmd + C.
更多信息：<https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- 将文件的内容放入剪贴板：

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将命令的执行结果放入剪贴板：

`find . -type t -name "*.png" | pbcopy`
