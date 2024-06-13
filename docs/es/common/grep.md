---
layout: page
title: common/grep (español)
description: "Encuentra patrones en archivos usando expresiones regulares."
content_hash: c132c4d4b951874b03c2a82ace54dbb7618350f3
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/grep.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/grep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

Encuentra patrones en archivos usando expresiones regulares.
Más información: <https://www.gnu.org/software/grep/manual/grep.html>.

- Busca un patrón dentro de un archivo:

`grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_busqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca una cadena exacta (desactiva las expresiones regulares):

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--fixed-strings</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_exacta</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca un patrón en todos los archivos de forma recursiva en un directorio, mostrando los números de línea de las coincidencias, ignorando los archivos binarios:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--line-number</span>` --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sin-parejamiento</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Utiliza expresiones regulares extendidas (admite `?`, `+`, `{}`, `()` y `|`), sin distinguir entre mayúsculas y minúsculas:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-E|--extended-regexp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--ignore-case</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime 3 líneas de contexto alrededor, antes o después de cada coincidencia:

`grep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime el nombre del archivo y el número de línea de cada coincidencia con salida en color:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--with-filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--line-number</span>` --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca líneas que coincidan con un patrón e imprime solo el texto coincidente:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--only-matching</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca `stdin` en las líneas que no coincidan con un patrón:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--invert-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_busqueda</span>`"`
