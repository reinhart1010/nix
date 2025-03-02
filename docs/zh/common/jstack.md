---
layout: page
title: common/jstack (中文)
description: "Java 栈跟踪工具。"
content_hash: 6d81b49de28f284997c6ccec18d2cba15fc41127
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jstack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jstack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jstack

Java 栈跟踪工具。
更多信息：<https://manned.org/jstack>.

- 打印 Java 进程中所有线程的 Java 栈跟踪：

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_进程号</span>

- 打印混合模式（Java/C++）的栈跟踪：

`jstack -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_进程号</span>

- 打印来自 Java 核心转储的栈跟踪：

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.core</span>
