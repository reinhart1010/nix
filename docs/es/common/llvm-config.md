---
layout: page
title: common/llvm-config (español)
description: "Obtiene variada información de configuración necesaria para compilar programas que utilizan LLVM."
content_hash: 13622f19c9c45019bbed21f3fd789ea1b0a8d119
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/llvm-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvm-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-config

Obtiene variada información de configuración necesaria para compilar programas que utilizan LLVM.
Típicamente llamado desde sistemas de construcción, como Makefiles o scripts de configuración.
Más información: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- Compila y vincula un programa basado en LLVM:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado_ejecutable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/source.cc</span>

- Imprime el `PREFIJO` de su instalación LLVM:

`llvm-config --prefix`

- Imprime todos los objetivos soportados por su LLVM instalado:

`llvm-config --targets-built`
