---
layout: page
title: common/javadoc (中文)
description: "从源代码以 HTML 格式生成 Java API 文档。"
content_hash: 701f94e713c94308ff716e86fd28dbb2d277f7cf
related_topics:
  - title: English version
    url: /en/common/javadoc.html
    icon: bi bi-globe
---
# javadoc

从源代码以 HTML 格式生成 Java API 文档。
更多信息：<https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>.

- 生成 Java 源代码的文档并将结果保存在文件夹中：

`javadoc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- 生成指定编码的文档：

`javadoc -docencoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- 生成文档时，排除掉某些软件包：

`javadoc -exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>
