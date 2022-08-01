---
layout: page
title: common/go-clean (中文)
description: "移除目标文件和缓存文件。"
content_hash: 558bae3954caf305eaf9e420823a69b0c197d850
related_topics:
  - title: English version
    url: /en/common/go-clean.html
    icon: bi bi-globe
---
# go clean

移除目标文件和缓存文件。
更多信息：<https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- 只打印移除命令，而不会真正移除任何东西：

`go clean -n`

- 删除编译缓存：

`go clean -cache`

- 删除所有测试结果缓存：

`go clean -testcache`

- 删除模块缓存：

`go clean -modcache`
