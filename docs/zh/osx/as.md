---
layout: page
title: osx/as (中文)
description: "便携式 GNU 汇编程序。"
content_hash: 9bb3b93812c2b968c0c7a4b7e2dc842b4701cbc9
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

便携式 GNU 汇编程序。
主要用于汇编 `gcc` 的输出以供 `ld` 使用。
更多信息：<https://keith.github.io/xcode-man-pages/as.1.html>.

- 汇编文件，将输出写入 a.out：

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.s</span>

- 将输出汇编到给定文件：

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.o</span>

- 通过跳过空白和注释预处理来更快地生成输出.（应该只用于受信任的编译器）：

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.s</span>

- 在目录列表中包含一个给定路径，以搜索 .include 指令中指定的文件：

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.s</span>
