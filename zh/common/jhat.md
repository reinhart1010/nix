---
layout: page
title: common/jhat (中文)
description: "Java 堆分析工具。"
content_hash: bff72c49b6ad8746d4f6ed3a83f5277dc65c5c18
related_topics:
  - title: English version
    url: /en/common/jhat.html
    icon: bi bi-globe
---
# jhat

Java 堆分析工具。
更多信息：<https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- 分析堆转储文件（来自 jmap），通过 http 端口 7000 进行查看：

`jhat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/堆转储文件</span>

- 分析堆转储文件，为 http 服务指定备用端口：

`jhat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/堆转储文件</span>

- 通过 jhat 分析转储文件，指定使用 8GB RAM（建议使用 2-4 倍的转储大小）：

`jhat -J-mx8G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/堆转储文件</span>
