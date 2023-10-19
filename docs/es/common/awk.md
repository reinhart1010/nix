---
layout: page
title: common/awk (español)
description: "Un lenguaje de programación versátil para trabajar con archivos."
content_hash: a6305b547b0cbc2b02aea00b0c1a85e5739de185
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
---
# awk

Un lenguaje de programación versátil para trabajar con archivos.
Más información: <https://github.com/onetrueawk/awk>.

- Imprime la quinta columna (también conocido como campo) en un archivo separado por espacios:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Imprime la segunda columna de las líneas que contengan "algo" en un archivo separado por espacios:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Imprime la última columna de cada línea de un archivo, usando la coma (en vez de espacio) como separador de campo:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Suma los valores en de la primera columna de un archivo e imprime el total:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Suma los valores en de la primera columna de un archivo e imprime el total de forma bonita:

`awk '{s+=$1; print $1} END {print "--------"; print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Imprime cada tres líneas, empezando por la primera:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Imprime todos los valores desde la tercera columna:

`awk '{for (i=3; i <= NF; i++) printf $i""FS; print""}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Imprime diferentes valores dependiendo de condiciones:

`awk '{if ($1 == "foo") print "Coincidencia completa foo"; else if ($1 ~ "bar") print "Coincidencia parcial bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>
