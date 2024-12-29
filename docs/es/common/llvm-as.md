---
layout: page
title: common/llvm-as (español)
description: "Ir de Representación intermedia LLVM (`.ll`) a Bitcode de Ensamblador  (`.bc`)."
content_hash: ce27b7f421fd2bc36710c9ed89b06e235a23f77b
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/llvm-as.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvm-as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-as

Ir de Representación intermedia LLVM (`.ll`) a Bitcode de Ensamblador  (`.bc`).
Más información: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- Ensambla un archivo IR:

`llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ensamblado.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/fuente.ll</span>

- Ensambla un archivo IR e incluye un hash de módulo en el archivo bitcode producido:

`llvm-as --module-hash -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ensamblado.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/fuente.ll</span>

- Lee un archivo IR de `stdin` y lo ensambla:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/fuente.ll</span>` | llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ensamblado.bc</span>
