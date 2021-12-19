---
layout: page
title: common/gradle (español)
description: "Gradle es un sistema de código abierto para automatizar la compilación de proyectos."
content_hash: f84867ab581a5a3cdcf57ee2ea32dd6f27258413
related_topics:
  - title: English version
    url: /en/common/gradle.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gradle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gradle

Gradle es un sistema de código abierto para automatizar la compilación de proyectos.
Más información: <https://gradle.org>.

- Compila un proyecto:

`gradle build`

- Excluye la tarea *test*:

`gradle build -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test</span>

- Ejecuta en modo offline para prevenir que Gradle acceda a la red durante una compilación:

`gradle build --offline`

- Limpia el directorio de compilación:

`gradle clean`

- Compila un paquete Android (APK) en modo lanzamiento:

`gradle assembleRelease`
