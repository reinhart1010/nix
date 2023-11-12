---
layout: page
title: common/jmap (English)
description: "Java memory map tool."
content_hash: 4d96fc95a6cbf0ea36166195439482bdb324ede0
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/jmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmap

Java memory map tool.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jmap.html>.

- Print shared object mappings for a Java process (output like pmap):

`jmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print heap summary information:

`jmap -heap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print histogram of heap usage by type:

`jmap -histo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Dump contents of the heap into a binary file for analysis with jhat:

`jmap -dump:format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Dump live objects of the heap into a binary file for analysis with jhat:

`jmap -dump:live,format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>
