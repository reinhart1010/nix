---
layout: page
title: common/go (中文)
description: "管理 Go 源代码的工具。"
content_hash: 9c2e71b1f8f75575257c92878fa0d4580048a433
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go

管理 Go 源代码的工具。
此命令也有关于其子命令的文件，例如：`go build`.
更多信息：<https://golang.org>.

- 下载并安装由其路径指定的包：

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/包</span>

- 编译并运行一个源文件（它必须包含一个 `main` 包）：

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.go</span>

- 将源文件编译为当前命名的可执行文件：

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.go</span>

- 编译当前目录中的包：

`go build`

- 执行当前包中的所有测试用例（文件必须以 `_test.go` 结尾）：

`go test`

- 编译并安装当前包：

`go install`

- 在当前目录下初始化一个新模块：

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模块</span>
