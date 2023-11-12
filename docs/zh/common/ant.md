---
layout: page
title: common/ant (中文)
description: "Apache Ant。"
content_hash: e6252de0ffe7248e614ffae8a2e010e8081f30ea
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant。
用于构建和管理基于 Java 的项目的工具。
更多信息：<https://ant.apache.org>.

- 用默认的构建文件 `build.xml` 构建一个项目：

`ant`

- 使用 `build.xml` 以外的构建文件构建项目：

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">构建文件.xml</span>

- 打印该项目可能的目标信息：

`ant -p`

- 打印调试信息：

`ant -d`

- 执行所有不依赖失败目标的目标：

`ant -k`
