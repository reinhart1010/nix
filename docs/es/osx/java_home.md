---
layout: page
title: osx/java_home (español)
description: "Devuelve un valor para $JAVA_HOME o ejecuta un comando usando esta variable."
content_hash: c73b8b15dcdebd524de5aa0d4ebb10c32fea8d70
last_modified_at: 2023-07-10
related_topics:
  - title: English version
    url: /en/osx/java_home.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># java_home

Devuelve un valor para $JAVA_HOME o ejecuta un comando usando esta variable.
Más información: <https://www.unix.com/man-page/osx/1/java_home>.

- Lista JVMs basadas en una versión específica:

`java_home --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.5+</span>

- Lista JVMs basadas en una [arch]itectura específica:

`java_home --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386</span>

- Lista JVMs basadas en tareas específicas (por defecto `CommandLine`):

`java_home --datamodel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Applets|WebStart|BundledApp|JNI|CommandLine</span>

- Lista JVMs en formato XML:

`java_home --xml`

- Muestra la ayuda:

`java_home --help`
