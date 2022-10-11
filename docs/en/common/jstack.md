---
layout: page
title: common/jstack (English)
description: "Java stack trace tool."
content_hash: 3d1635e471d7b825135da1d5635d12f227141040
---
# jstack

Java stack trace tool.
More information: <https://manned.org/jstack>.

- Print Java stack traces for all threads in a Java process:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print mixed mode (Java/C++) stack traces for all threads in a Java process:

`jstack -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_pid</span>

- Print stack traces from Java core dump:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.core</span>
