---
layout: page
title: common/javac (English)
description: "Java application compiler."
content_hash: a4d4837c156914d51184cc3dddd3ec8b3511580c
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/javac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/javac.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/javac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javac

Java application compiler.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- Compile a `.java` file:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.java</span>

- Compile several `.java` files:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.java</span>

- Compile all `.java` files in current directory:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- Compile a `.java` file and place the resulting class file in a specific directory:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.java</span>
