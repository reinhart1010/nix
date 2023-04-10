---
layout: page
title: common/asar (español)
description: "Un archivador de ficheros para la plataforma Electron."
content_hash: 773170194c167f400a82e81c48ca98f6f616eb0e
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/asar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/asar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asar.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/asar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># asar

Un archivador de ficheros para la plataforma Electron.
Más información: <https://github.com/electron/asar>.

- Archiva un fichero o directorio:

`asar pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivado.asar</span>

- Extrae un archivo:

`asar extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivado.asar</span>

- Extrae un archivo específico de un archivo:

`asar extract-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivado.asar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Lista el contenido de un archivo:

`asar list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivado.asar</span>
