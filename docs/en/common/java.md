---
layout: page
title: common/java (English)
description: "Java application launcher."
content_hash: b523db9f9192bf4db243bc49533c0d512763fe89
last_modified_at: 2024-01-30
related_topics:
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
tldri18n_status: 2
---
# java

Java application launcher.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- Execute a Java `.class` file that contains a main method by using just the class name:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classname</span>

- Execute a Java program and use additional third-party or user-defined classes:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/classes1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/classes2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classname</span>

- Execute a `.jar` program:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.jar</span>

- Execute a `.jar` program with debug waiting to connect on port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.jar</span>

- Display JDK, JRE and HotSpot versions:

`java -version`

- Display help:

`java -help`
