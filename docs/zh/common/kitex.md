---
layout: page
title: common/kitex (中文)
description: "Kitex 是 Go RPC 框架 Kitex 框架提供的用于生成代码的一个命令行工具。"
content_hash: 89ab5a711754dda5b7b9f62dbb9d9c60a06cbab9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/kitex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kitex

Kitex 是 Go RPC 框架 Kitex 框架提供的用于生成代码的一个命令行工具。
目前，kitex 支持 thrift 和 protobuf 的 IDL，并支持生成一个服务端项目的骨架。
更多信息：<https://www.cloudwego.io>.

- 生成客户端代码，项目在 `$GOPATH` 目录下：

`kitex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/IDL文件.thrift</span>

- 生成客户端代码，项目不在 `$GOPATH` 目录下：

` kitex -module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/xx-org/xx-name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/IDL文件.thrift</span>

- 根据 protobuf IDL 文件生成客户端代码：

`kitex -type protobuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/IDL文件.proto</span>

- 生成服务端代码：

`kitex -service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svc_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/IDL文件.thrift</span>
