---
layout: page
title: common/hexdump (español)
description: "Un visor ASCII, decimal, hexadecimal, octal."
content_hash: d46822d87d6883db58393b45db6052a73b5751f6
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/hexdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexdump

Un visor ASCII, decimal, hexadecimal, octal.
Más información: <https://manned.org/hexdump>.

- Imprime la representación hexadecimal de un archivo, reemplazando líneas duplicadas con '*':

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra el desplazamiento de entrada (input offset) en hexadecimal y su representación ASCII en dos columnas:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra la representación hexadecimal de un archivo, pero interpreta solo n bytes de la entrada:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- No reemplaza las líneas duplicadas con '*':

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
