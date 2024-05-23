---
layout: page
title: common/tree (中文)
description: "以树的形式显示当前目录的内容。"
content_hash: 66cd8bd8128013292f786d9ecafa6224db37d029
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tree

以树的形式显示当前目录的内容。
更多信息：<https://manned.org/man/tree>.

- 显示深度达到 “级数” 级的文件和目录（其中 1 表示当前目录）：

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">级数</span>

- 只显示目录：

`tree -d`

- 同时显示隐藏文件：

`tree -a`

- 打印没有缩进行的树，显示完整路径（使用`-N`不转义空格和特殊字符）：

`tree -i -f`

- 以可读格式打印每个文件节点的大小，目录显示其累积大小（类似在`du`命令中所示）：

`tree -s -h --du`

- 使用通配符（glob）模式在树层次结构中查找文件，并删除不包含匹配文件的目录：

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- 在树层次结构中查找目录，删除不属于所需目录的目录：

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹名</span>` --matchdirs --prune`
