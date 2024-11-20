---
layout: page
title: common/quarkus (中文)
description: "创建 Quarkus 项目，管理扩展并执行基本的构建和开发任务。"
content_hash: 707f072a1b996e5b2fceee4ed8164b14719e448c
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/quarkus.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/quarkus.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/quarkus.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quarkus

创建 Quarkus 项目，管理扩展并执行基本的构建和开发任务。
更多信息：<https://quarkus.io/guides/cli-tooling>.

- 在一个新目录中创建一个新的应用程序项目：

`quarkus create app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">项目名称</span>

- 在实时编码模式下运行当前项目：

`quarkus dev`

- 运行应用程序：

`quarkus run`

- 在连续测试模式下运行当前项目：

`quarkus test`

- 向当前项目添加一个或多个扩展：

`quarkus extension add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">扩展名1 扩展名2 ...</span>

- 使用 Docker 构建容器镜像：

`quarkus image build docker`

- 将应用程序部署到 Kubernetes：

`quarkus deploy kubernetes`

- 更新项目：

`quarkus update`
