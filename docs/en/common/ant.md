---
layout: page
title: common/ant (English)
description: "Apache Ant."
content_hash: a0d53afc0f986c53db4f300d1d7c3fbb9c7da70a
last_modified_at: 2024-02-09
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant.
Tool for building and managing Java-based projects.
More information: <https://ant.apache.org>.

- Build a project with default build file `build.xml`:

`ant`

- Build a project using build [f]ile other than `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- Print information on possible targets for this project:

`ant -p`

- Print debugging information:

`ant -d`

- Execute all targets that do not depend on fail target(s):

`ant -k`
