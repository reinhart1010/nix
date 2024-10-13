---
layout: page
title: common/javac (中文)
description: "Java 程序编译器。"
content_hash: 2959c315e10baa3141cbf942f0388b37ff7bb450
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/javac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/javac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/javac.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/javac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javac

Java 程序编译器。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- 编译一个 `.java` 文件：

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.java</span>

- 编译多个 `.java` 文件：

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名1.java 文件名2.java 文件名3.java ...</span>

- 编译当前目录内所有 `.java` 文件：

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- 编译一个 `.java` 文件并将生成的 class 字节码文件放入一个指定目录：

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.java</span>
