---
layout: page
title: common/valgrind (español)
description: "Programa para un conjunto de herramientas expertas con programas de perfilado, optimización y depuración."
content_hash: f1460fbdf1440003dcf838a7000f16d5755e0027
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/valgrind.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/valgrind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# valgrind

Programa para un conjunto de herramientas expertas con programas de perfilado, optimización y depuración.
Entre las herramientas de uso común cabe citar: `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind` y `drd`.
Más información: <https://www.valgrind.org>.

- Utiliza la herramienta Memcheck (por defecto) para mostrar un diagnóstico del uso de la memoria por `programa`:

`valgrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Utiliza Memcheck para informar sobre todas las posibles fugas de memoria de `programa` en detalle:

`valgrind --leak-check=full --show-leak-kinds=all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Utiliza la herramienta Cachegrind para perfilar y registrar operaciones de caché de CPU de `programa`:

`valgrind --tool=cachegrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Utiliza la herramienta Massif para perfilar y registrar la memoria heap y el uso de la pila de `programa`:

`valgrind --tool=massif --stacks=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>
