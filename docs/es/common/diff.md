---
layout: page
title: common/diff (español)
description: "Compara archivos y directorios."
content_hash: 7df9c90155096b30975f1b5311d00c742b601358
last_modified_at: 2024-06-19
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># diff

Compara archivos y directorios.
Más información: <https://manned.org/diff>.

- Compara archivos (lista los cambios para convertir `archivo_viejo` en `archivo_nuevo`):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>

- Compara archivos, ignorando los espacios en blanco:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|--ignore-all-space</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>

- Compara archivos, mostrando las diferencias lado a lado:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--side-by-side</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>

- Compara archivos, mostrando las diferencias en formato unificado (como el que usa `git diff`):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unified</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>

- Compara directorios de forma recursiva (muestra los nombres de los archivos/directorios que difieran y los cambios realizados en los archivos):

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_nuevo</span>

- Compara directorios, mostrando solo los nombres de los archivos que difieren:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-q|--brief</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_nuevo</span>

- Crea un archivo de revisión para Git a partir de las diferencias entre dos archivos de texto, tratando los archivos inexistentes como vacíos:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--text</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unified</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-N|--new-file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.patch</span>

- Compara archivos, mostrando la salida en color y se esfuerza por encontrar el conjunto más pequeño de cambios:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--minimal</span>` --color=always `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_viejo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_nuevo</span>
