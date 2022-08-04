---
layout: page
title: osx/popd (中文)
description: "通过 pushd shell 内置程序删除目录堆栈中的目录。"
content_hash: d8c8f87f3e283e774793b573db31cb9af4b9c8b1
---
# popd

通过 pushd shell 内置程序删除目录堆栈中的目录。

- 从堆栈中删除顶部目录，并用 `cd` 跳转到该目录：

`popd`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd +N`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表右侧开始）：

`popd -N`
