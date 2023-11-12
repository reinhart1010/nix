---
layout: page
title: common/jps (中文)
description: "显示当前用户的 JVM 进程状态。"
content_hash: 9592e35115cbcd96bf7caa52381e23f41e7a8207
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/jps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jps

显示当前用户的 JVM 进程状态。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jps.html>.

- 列出所有 JVM 进程：

`jps`

- 列出所有 JVM 进程，只打印进程号：

`jps -q`

- 显示传递给进程的参数：

`jps -m`

- 显示所有进程的完整软件包名称：

`jps -l`

- 显示传递给 JVM 的参数：

`jps -v`
