---
layout: page
title: common/qc (中文)
description: "管理和执行存储在 QOwnNotes 笔记中的命令片段。"
content_hash: c9eb920e37c8e892917b7119c7539d72ceb6f7a6
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qc

管理和执行存储在 QOwnNotes 笔记中的命令片段。
请参阅：`qownnotes`.
更多信息：<https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

- 配置代码片段管理器，例如设置来自 QOwnNotes 的安全令牌：

`qc configure`

- 搜索并打印存储在 `Commands.md` 笔记中的命令片段以及所有标记为 `commands` 的笔记：

`qc search`

- 执行一个片段并在执行前显示命令：

`qc exec --command`

- 执行上一个片段并在执行前显示命令：

`qc exec --command --last`

- 在 QOwnNotes 中切换笔记文件夹：

`qc switch`
