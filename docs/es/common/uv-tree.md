---
layout: page
title: common/uv-tree (español)
description: "Muestra las dependencias del proyecto en formato de árbol."
content_hash: 5c8fcd4116bed27a14e46835c0e61caac34eafca
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uv-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv tree

Muestra las dependencias del proyecto en formato de árbol.
Más información: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- Muestra el árbol de dependencias del entorno actual:

`uv tree`

- Muestra el árbol de dependencias para todos los entornos:

`uv tree --universal`

- Muestra el árbol de dependencias hasta una determinada profundidad:

`uv tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--depth</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Muestra la última versión disponible para todos los paquetes obsoletos:

`uv tree --outdated`

- Excluye dependencias del grupo dev:

`uv tree --no-dev`

- Muestra el árbol invertido, para que los hijos sean dependientes en lugar de dependencias:

`uv tree --invert`
