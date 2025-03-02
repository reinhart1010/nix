---
layout: page
title: common/jmap (中文)
description: "Java 内存映射工具。"
content_hash: 09c7aa929af72d7d02c0a775bd431c5afe83c5ad
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jmap.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmap

Java 内存映射工具。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

- 打印 Java 进程的共享对象映射（类似 pmap 的输出）：

`jmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 打印堆摘要信息：

`jmap -heap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 按类型打印堆使用的直方图：

`jmap -histo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 将堆的内容转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 将堆中存活的对象转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:live,format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>
