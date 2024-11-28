---
layout: page
title: common/objdump (español)
description: "Muestra información sobre los archivos objeto."
content_hash: efd849f1a319819cf5f5932a24feca344e38f9c7
last_modified_at: 2024-11-28
related_topics:
  - title: English version
    url: /en/common/objdump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/objdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/objdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# objdump

Muestra información sobre los archivos objeto.
Más información: <https://manned.org/objdump>.

- Muestra la información del encabezado del archivo:

`objdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra toda la información del encabezado:

`objdump -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra la salida desensamblada (disassembled) de secciones ejecutables:

`objdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra las secciones ejecutables desensambladas con sintaxis Intel:

`objdump -M intel -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra un volcado hexadecimal ruta/al/binario completo de todas las secciones:

`objdump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>
