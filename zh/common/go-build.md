---
layout: page
title: common/go-build (中文)
description: "编译 Go 源代码。"
content_hash: 6e3d3673494e55cf21a5fd9c2137592a03d6b771
related_topics:
  - title: English version
    url: /en/common/go-build.html
    icon: bi bi-globe
---
# go build

编译 Go 源代码。
更多信息：<https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- 编译‘package main’文件（输出为不带扩展名的文件名）：

`go build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/main.go</span>

- 编译，并指定输出文件名：

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/二进制文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件.go</span>

- 编译一个包：

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/二进制文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/包</span>

- 编译 main 包为可执行文件，并开启数据竞态检测：

`go build -race -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/可执行文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/main/包</span>
