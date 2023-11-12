---
layout: page
title: common/ant (English)
description: "Apache Ant."
content_hash: f8a4c14e106e32e6863ba4dd11c3865ad45c5de6
last_modified_at: 2023-11-12
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

- Build a project using build file other than `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- Print information on possible targets for this project:

`ant -p`

- Print debugging information:

`ant -d`

- Execute all targets that do not depend on fail target(s):

`ant -k`
