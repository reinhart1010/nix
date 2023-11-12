---
layout: page
title: common/adscript (中文)
description: "用于 Adscript 文件的编译器。"
content_hash: b103990bcc0507adbc52a66f1489d54a4e803d7b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/adscript.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/adscript.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adscript.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adscript.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adscript

用于 Adscript 文件的编译器。
更多信息：<https://github.com/Amplus2/Adscript>.

- 将一个文件编译为一个对象文件：

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.adscript</span>

- 编译并链接一个文件到一个独立的可执行文件：

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.adscript</span>

- 将文件编译成 LLVM IR 而不是本地机器码：

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.adscript</span>

- 将一个文件交叉编译为一个其他 CPU 架构或操作系统的目标文件：

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.adscript</span>
