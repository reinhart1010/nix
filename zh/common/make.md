---
layout: page
title: common/make (中文)
description: "Makefile 文件描述目标的任务运行器。"
content_hash: dce568fd2464807acd6e84fa1e2dd6f2f7053e87
related_topics:
  - title: English version
    url: /en/common/make.html
    icon: bi bi-globe
---
# make

Makefile 文件描述目标的任务运行器。
通常用于控制源代码中可执行文件的编译。
更多信息：<https://www.gnu.org/software/make/manual/make.html>.

- 调用 Makefile 中指定的第一个目标（通常命名为 "all"）：

`make`

- 调用指定目标：

`make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 调用一个指定的目标，一次并行执行 4 个作业：

`make -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 使用指定的 Makefile 文件：

`make --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 从另一个目录执行 make ：

`make --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件夹</span>

- 即使源文件未更改，也强制执行目标：

`make --always-make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 覆盖在 Makefile 中定义的环境变量：

`make --environment-overrides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>
