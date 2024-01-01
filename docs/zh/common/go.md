---
layout: page
title: common/go (中文)
description: "管理 Go 源代码的工具。"
content_hash: 494f0a50eb5e1fc40d78268c5ed2b4b4264390e8
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go

管理 Go 源代码的工具。
此命令也有关于其子命令的文件，例如：`go build`.
更多信息：<https://golang.org>.

- 下载并安装由其路径指定的包：

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/包</span>

- 编译并运行一个源文件（它必须包含一个 `main` 包）：

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>`.go`

- 将源文件编译为当前命名的可执行文件：

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可执行文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>`.go`

- 编译当前目录中的包：

`go build`

- 执行当前包中的所有测试用例（文件必须以 `_test.go` 结尾）：

`go test`

- 编译并安装当前包：

`go install`

- 在当前目录下初始化一个新模块：

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模块</span>
