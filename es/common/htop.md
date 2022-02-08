---
layout: page
title: common/htop (español)
description: "Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`."
content_hash: 958d19b60e45f9bfd42ba5d9f841673aca8d3c7f
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/htop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
