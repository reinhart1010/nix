---
layout: page
title: common/jdeps (中文)
description: "Java 类依赖分析器。"
content_hash: eb19a0200cbc31aaec0aea69c02095a295276dec
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jdeps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jdeps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jdeps

Java 类依赖分析器。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>.

- 分析 `.jar` 或 `.class` 文件的依赖关系：

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件名.class</span>

- 打印特定 `.jar` 文件的所有依赖关系摘要：

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件名.jar</span>` -summary`

- 打印 `.jar` 文件的所有类级依赖关系：

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件名.jar</span>` -verbose`

- 将分析结果输出为 DOT 文件到指定目录：

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件名.jar</span>` -dotoutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 显示帮助信息：

`jdeps --help`
