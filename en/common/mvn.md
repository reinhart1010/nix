---
layout: page
title: common/mvn (English)
description: "Apache Maven."
content_hash: 57f6d07e3c92bf3de101f2e09327cd00ea4fede8
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/mvn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mvn.html
    icon: bi bi-globe
---
# mvn

Apache Maven.
Tool for building and managing Java-based projects.
More information: <https://maven.apache.org>.

- Compile a project:

`mvn compile`

- Compile and package the compiled code in its distributable format, such as a `jar`:

`mvn package`

- Compile and package, skipping unit tests:

`mvn package -DskipTests`

- Install the built package in local maven repository. (This will invoke the compile and package commands too):

`mvn install`

- Delete build artifacts from the target directory:

`mvn clean`

- Do a clean and then invoke the package phase:

`mvn clean package`

- Clean and then package the code with a given build profile:

`mvn clean -P`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>` package`

- Run a class with a main method:

`mvn exec:java -Dexec.mainClass="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.Main</span>`" -Dexec.args="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2</span>`"`
