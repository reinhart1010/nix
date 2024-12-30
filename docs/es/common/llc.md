---
layout: page
title: common/llc (español)
description: "Compila Representación intermedia LLVM o código bit (bitcode) para el lenguaje ensamblador objetivo específico."
content_hash: 484959dc6d497c53099c811ca2e2f2f0e8045441
last_modified_at: 2024-12-30
related_topics:
  - title: English version
    url: /en/common/llc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llc

Compila Representación intermedia LLVM o código bit (bitcode) para el lenguaje ensamblador objetivo específico.
Más información: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- Compila un bitcode o archivo IR a un archivo ensamblador con el mismo nombre base:

`llc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>

- Habilita todas las optimizaciones:

`llc -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>

- Dirige la salida a un archivo específico:

`llc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.s</span>

- Emite código, independiente de la posición que pueda reubicarse completamente:

`llc -relocation-model=pic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.ll</span>
