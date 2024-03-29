---
layout: page
title: osx/afinfo (español)
description: "Analizador de metadatos de archivos de audio para OS X."
content_hash: 8385c00d8ef043c21c35984c9e006db1c9cd311b
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/afinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afinfo

Analizador de metadatos de archivos de audio para OS X.
Comando nativo de OS X.
Más información: <https://keith.github.io/xcode-man-pages/afinfo.1.html>.

- Muestra información de un archivo de audio dado:

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra una descripción de una línea del archivo de audio:

`afinfo --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra información de metadatos y contenido del InfoDictionary del archivo de audio:

`afinfo --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la salida en formato XML:

`afinfo --xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra advertencias para el archivo de audio, si las hubiera:

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra ayuda para un uso completo:

`afinfo --help`
