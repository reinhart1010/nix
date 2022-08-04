---
layout: page
title: common/jmap (中文)
description: "Java 内存映射工具。"
content_hash: f4c0dea2bb8c96054e9412cda9ccead83f1e16bb
related_topics:
  - title: English version
    url: /en/common/jmap.html
    icon: bi bi-globe
---
# jmap

Java 内存映射工具。
更多信息：<https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html>.

- 打印 Java 进程的共享对象映射（类似 pmap 的输出）：

`jmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 打印堆摘要信息：

`jmap -heap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 按类型打印堆使用的直方图：

`jmap -histo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>

- 将堆的内容转储到二进制文件中以使用 jhat 进行分析：

`jmap -dump:format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导出文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 进程号</span>
