---
layout: page
title: common/htop (español)
description: "Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`."
content_hash: f41a8f3993de03be7930be499b410c906ac184ba
last_modified_at: 2024-11-03
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
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htop

Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`.
Más información: <https://htop.dev/>.

- Inicia `htop`:

`htop`

- Inicia `htop` mostrando solo los procesos pertenecientes a un usuario dado:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Muestra procesos jerárquicamente en una vista de árbol para visibilizar las relaciones entre padres e hijos:

`htop --tree`

- Ordena procesos especificando un `criterio_de_ordenamiento` (usa `htop --sort help` para ver las opciones disponibles):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_ordenamiento</span>

- Inicia `htop` con una espera dada entre las actualizaciones, en décimas de segundo (es decir, 50 = 5 segundos):

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Muestra comandos interactivos mientras se está ejecutando `htop`:

`?`

- Cambia a otro panel:

`tab`

- Muestra la ayuda:

`htop --help`
