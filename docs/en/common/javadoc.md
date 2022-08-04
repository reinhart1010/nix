---
layout: page
title: common/javadoc (English)
description: "Generate Java API documentation in HTML format from source code."
content_hash: ad5dce307bca23757d15ee64eae6db3b58af96bf
related_topics:
  - title: 中文 version
    url: /zh/common/javadoc.html
    icon: bi bi-globe
---
# javadoc

Generate Java API documentation in HTML format from source code.
More information: <https://docs.oracle.com/javase/9/javadoc/javadoc-command.htm>.

- Generate documentation for Java source code and save the result in a directory:

`javadoc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- Generate documentation with a specific encoding:

`javadoc -docencoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>

- Generate documentation excluding some packages:

`javadoc -exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/java_source_code</span>
