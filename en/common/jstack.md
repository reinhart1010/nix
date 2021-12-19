---
layout: page
title: common/jstack (English)
description: "Java Stack Trace Tool."
content_hash: 8fa4b3c3792d607379dfa6e2f2fc3dd6c16af6dd
---
# jstack

Java Stack Trace Tool.
More information: <https://manned.org/jstack>.

- Print Java stack traces for all threads in a Java process:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print mixed mode (Java/C++) stack traces for all threads in a Java process:

`jstack -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print stack traces from Java core dump:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.core</span>
