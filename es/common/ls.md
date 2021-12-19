---
layout: page
title: common/ls (español)
description: "Lista los contenidos de directorios."
content_hash: c2f034c0c9edbabefcc30d30382aa0411f37e518
related_topics:
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ls

Lista los contenidos de directorios.
Más información: <https://www.gnu.org/software/coreutils/ls>.

- Lista un archivo por línea:

`ls -1`

- Lista todos los archivos, incluyendo archivos ocultos:

`ls -a`

- Lista todos los archivos, añadiendo `/` al final de los nombres de directorios:

`ls -F`

- Lista todos los archivos con formato largo (permisos, propietario, tamaño y fecha de modificación):

`ls -la`

- Lista con formato largo y tamaño legible por humanos (KiB, MiB, GiB):

`ls -lh`

- Lista con formato largo y tamaño en orden descendente:

`ls -lS`

- Lista todos los archivos con formato largo, ordenado por fecha de modificación (archivos más viejos en primer lugar):

`ls -ltr`
