---
layout: page
title: common/java (中文)
description: "Java 程序启动器。"
content_hash: b09bf4400c5ff8b7b77e58235a04dffd2a81bec2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/java.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># java

Java 程序启动器。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- 通过提供类名称运行一个含有 main 函数的 java .class 程序：

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类名称</span>

- 运行一个 .jar 程序：

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.jar</span>

- 运行一个 .jar 程序并且在端口 5005 等待调试器：

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.jar</span>

- 显示 JDK, JRE 和 HotSpot 的版本：

`java -version`

- 显示详细的帮助：

`java -help`
