---
layout: page
title: common/jmap (English)
description: "Java Memory Map Tool."
content_hash: df473201b6af0eaf9ab881df04dcb85e12be6904
related_topics:
  - title: 中文 version
    url: /zh/common/jmap.html
    icon: bi bi-globe
---
# jmap

Java Memory Map Tool.
More information: <https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html>.

- Print shared object mappings for a Java process (output like pmap):

`jmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print heap summary information:

`jmap -heap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print histogram of heap usage by type:

`jmap -histo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Dump contents of the heap into a binary file for analysis with jhat:

`jmap -dump:format=b,file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>
