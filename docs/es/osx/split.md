---
layout: page
title: osx/split (español)
description: "Divide un archivo en trozos."
content_hash: 559350f471cf322e81c260e64ea2af49da2ebfff
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/split.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

Divide un archivo en trozos.
Más información: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Divide un archivo, cada división tiene 10 líneas (excepto la última división):

`split -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>

- Divide un fichero mediante una expresión regular. La línea que coincida será la primera línea del siguiente archivo de salida:

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>

- Divide un archivo con 512 bytes en cada división (excepto en la última; utiliza 512k para kilobytes y 512m para megabytes):

`split -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>

- Divide un archivo en 5 archivos. El archivo se divide de forma que cada división tenga el mismo tamaño (excepto la última división):

`split -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>
