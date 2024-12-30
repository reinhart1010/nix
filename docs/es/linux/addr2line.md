---
layout: page
title: linux/addr2line (español)
description: "Convierte direcciones de un binario en nombres de archivos y números de línea."
content_hash: 8afe20b07e865d9645c9a73965ce8c5c423f5ac2
last_modified_at: 2024-12-30
related_topics:
  - title: Deutsch version
    url: /de/linux/addr2line.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/addr2line.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addr2line

Convierte direcciones de un binario en nombres de archivos y números de línea.
Más información: <https://manned.org/addr2line>.

- Muestra el nombre de archivo y el número de línea del código fuente desde una dirección de instrucción de un ejecutable:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ejecutable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección</span>

- Muestra el nombre de la función, nombre de archivo y número de línea:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ejecutable</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección</span>

- Decodifica (demangle) el nombre de la función para código C++:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ejecutable</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección</span>
