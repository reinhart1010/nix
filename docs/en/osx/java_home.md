---
layout: page
title: osx/java_home (English)
description: "Return a value for $JAVA_HOME or execute command using this variable."
content_hash: 379d377481ce3e10aaa1f290fe95863f1cb7a7c3
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/java_home.html
    icon: bi bi-globe
tldri18n_status: 2
---
# java_home

Return a value for $JAVA_HOME or execute command using this variable.
More information: <https://www.unix.com/man-page/osx/1/java_home>.

- List JVMs based on a specific version:

`java_home --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.5+</span>

- List JVMs based on a specific [arch]itecture:

`java_home --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386</span>

- List JVMs based on a specific tasks (defaults to `CommandLine`):

`java_home --datamodel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Applets|WebStart|BundledApp|JNI|CommandLine</span>

- List JVMs in a XML format:

`java_home --xml`

- Display help:

`java_home --help`
