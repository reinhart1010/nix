---
layout: page
title: common/javadoc (中文)
description: "从源代码以 HTML 格式生成 Java API 文档。"
content_hash: 9e5cd142f8a327915eb6bff64874a8da6faf7c02
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/javadoc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/javadoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javadoc

从源代码以 HTML 格式生成 Java API 文档。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javadoc.html>.

- 生成 Java 源代码的文档并将结果保存在文件夹中：

`javadoc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- 生成指定编码的文档：

`javadoc -docencoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- 生成文档时，排除掉某些软件包：

`javadoc -exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>
