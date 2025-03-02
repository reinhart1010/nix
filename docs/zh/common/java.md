---
layout: page
title: common/java (中文)
description: "Java 程序启动器。"
content_hash: c0e358ec4751c9821a5efafad28363686af55788
last_modified_at: 2025-03-02
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
tldri18n_status: 2
---
# java

Java 程序启动器。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- 通过提供类名称运行一个含有 main 函数的 java `.class` 程序：

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类名称</span>

- 运行 Java 程序，并使用附加的第三方或用户定义类：

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/类1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/类2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类名称</span>

- 运行一个 `.jar` 程序：

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.jar</span>

- 运行一个 `.jar` 程序并且在端口 5005 等待调试器：

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.jar</span>

- 显示 JDK、JRE 和 HotSpot 的版本：

`java -version`

- 显示帮助：

`java -help`
