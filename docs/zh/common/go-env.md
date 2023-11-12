---
layout: page
title: common/go-env (中文)
description: "管理 Go 工具链使用的环境变量。"
content_hash: aa63361715d066c5d7fd2816881c2508d1cbf584
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-env.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go env

管理 Go 工具链使用的环境变量。
更多信息：<https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- 显示所有环境变量：

`go env`

- 显示指定的环境变量：

`go env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOPATH</span>

- 设置某个环境变量为指定值：

`go env -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 重置某个环境变量的值：

`go env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>
