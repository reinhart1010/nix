---
layout: page
title: common/ack (español)
description: "Una herramienta de búsqueda como grep, optimizada para desarrolladores."
content_hash: c664b960a36beb34e70bdfba154c7b4c558b2cb3
last_modified_at: 2024-05-05
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Una herramienta de búsqueda como grep, optimizada para desarrolladores.
Vea también: `rg`, que es más rápido.
Más información: <https://beyondgrep.com/documentation>.

- Busca archivos que contengan una cadena o expresión regular en el directorio actual de forma recursiva:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Busca un patrón sin distinción entre mayúsculas y minúsculas:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Busca líneas que coincidan con un patrón, imprimiendo s[o]lamente el texto coincidente y no el resto de la línea:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Limita la búsqueda a archivos de un tipo específico:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Busca archivos que no sean de un cierto tipo:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Cuenta el número total de coincidencias encontradas:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Imprime sólo los nombres de los archivos y el número de coincidencias de cada archivo:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`"`

- Lista todos los valores que se pueden utilizar con `--type`:

`ack --help-types`
