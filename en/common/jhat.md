---
layout: page
title: common/jhat (English)
description: "Java Heap Analysis Tool."
content_hash: cbd067d81ad6cc5a34ea3ac7e718b66711d2f568
related_topics:
  - title: 中文 version
    url: /zh/common/jhat.html
    icon: bi bi-globe
---
# jhat

Java Heap Analysis Tool.
More information: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- Analyze a heap dump (from `jmap`), view via HTTP on port 7000:

`jhat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dump_file.bin</span>

- Analyze a heap dump, specifying an alternate port for the http server:

`jhat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dump_file.bin</span>

- Analyze a dump letting `jhat` use up to 8 GB RAM (2-4x dump size recommended):

`jhat -J-mx8G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dump_file.bin</span>
