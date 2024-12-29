---
layout: page
title: common/llvm-dis (español)
description: "Convierte archivos LLVM de bitcode en representación intermedia (IR) LLVM legible."
content_hash: c62aea3a9d472891f8805e03afeaaa087b84ab78
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/llvm-dis.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvm-dis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-dis

Convierte archivos LLVM de bitcode en representación intermedia (IR) LLVM legible.
Más información: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- Convierte un archivo bitcode como LLVM IR y escribe el resultado en `stdout`:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.bc</span>` -o -`

- Convierte un archivo bitcode en un archivo LLVM IR con el mismo nombre de archivo:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bc</span>

- Convierte un archivo bitcode en LLVM IR, escribe el resultado al archivo especificado:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.bc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ll</span>
