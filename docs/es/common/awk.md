---
layout: page
title: common/awk (español)
description: "Un versátil lenguaje de programación para trabajar con archivos."
content_hash: aa3f0ede0547247fcd1f6de432d1df9d74777dce
last_modified_at: 2024-10-07
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
  - title: Nederlands version
    url: /nl/common/awk.html
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
tldri18n_status: 2
---
# awk

Un versátil lenguaje de programación para trabajar con archivos.
Más información: <https://github.com/onetrueawk/awk>.

- Imprime la quinta columna (también conocida como campo) de un archivo separado por espacios:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la segunda columna de las líneas que contienen "foo" en un archivo separado por espacios:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la última columna de cada línea de un archivo, utilizando una coma (en lugar de un espacio) como separador de campos:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Suma los valores de la primera columna de un fichero e imprime el total:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime una de cada tres líneas a partir de la primera:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime diferentes valores basados en condiciones:

`awk '{if ($1 == "foo") print "Coincidencia exacta foo"; else if ($1 ~ "bar") print "Coincidencia parcial bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime todas las líneas en las que el valor de la 10ª columna está entre un mínimo y un máximo:

`awk '($10 >= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_mínimo</span>` && $10 <= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_máximo</span>`)'`

- Imprime tabla de usuarios con UID >=1000 con cabecera y salida formateada, usando dos puntos como separador (`%-20s` significa: 20 caracteres de cadena alineados a la izquierda, `%6s` significa: 6 caracteres de cadena alineados a la derecha):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
