---
layout: page
title: common/ar (español)
description: "Crea, modifica y extrae de archivos Unix. Típicamente utilizado para bibliotecas estáticas (`.a`) y paquetes Debian (`.deb`)."
content_hash: 1285a12223a208844efe9aba3532986b8406e685
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ar

Crea, modifica y extrae de archivos Unix. Típicamente utilizado para bibliotecas estáticas (`.a`) y paquetes Debian (`.deb`).
Vea también: `tar`, `ranlib`.
Más información: <https://manned.org/ar>.

- E[x]trae todos los miembros de un archivo:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.a</span>

- Lis[t]a los contenidos de un archivo:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ar</span>

- [r]eemplaza o añade archivos a un archivo:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/binario-debian ruta/a/control.tar.gz ruta/a/datos.tar.xz ...</span>

- In[s]erta un índice de archivo objeto (equivalente a usar `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.a</span>

- Crea un archivo con archivos específicos incluyendo un índice de archivo objeto:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.o ruta/al/archivo2.o ...</span>
