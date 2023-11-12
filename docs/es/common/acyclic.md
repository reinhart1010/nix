---
layout: page
title: common/acyclic (español)
description: "Hace un gráfico acíclico invirtiendo algunos bordes."
content_hash: 58c01ef69a68c2f9ff3cd7f03ccf739d19d9a0ef
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acyclic

Hace un gráfico acíclico invirtiendo algunos bordes.
Filtros Graphviz: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
Más información: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Hace un gráfico acíclico invirtiendo algunos bordes:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.gv</span>

- Imprime si un gráfico es acíclico, tiene un ciclo o si no posee instrucciones, no genera ningún gráfico de salida:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.gv</span>

- Mostrar ayuda para `acyclic`:

`acyclic -?`
