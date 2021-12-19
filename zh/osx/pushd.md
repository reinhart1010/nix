---
layout: page
title: osx/pushd (中文)
description: "将目录放在堆栈上，以便以后访问。"
content_hash: 07286754714120c4db6f06241a6eaa6e7bc32bb8
---
# pushd

将目录放在堆栈上，以便以后访问。
另请参阅 `popd` 命令说明，以切换回原始目录。

- 切换到目录并将其添加到堆栈上：

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- 切换堆栈上的第一个和第二个目录：

`pushd`

- 通过使第 5 个元素成为堆栈的顶部来旋转堆栈：

`pushd +4`
