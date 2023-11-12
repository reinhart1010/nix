---
layout: page
title: common/htop (español)
description: "Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`."
content_hash: 958d19b60e45f9bfd42ba5d9f841673aca8d3c7f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`.
Más información: <https://htop.dev/>.

- Inicia htop:

`htop`

- Inicia htop mostrando solo procesos pertenecientes a un usuario dado:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Ordena procesos por un específico `elemento_de_ordenamiento` (use `htop --sort help` para opciones disponibles):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elemento_de_ordenamiento</span>

- Muestra comandos interactivos mientras corre htop:

`?`

- Muestra la ayuda:

`htop --help`
