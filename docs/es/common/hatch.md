---
layout: page
title: common/hatch (español)
description: "Gestor de proyectos Python moderno y extensible."
content_hash: 60979769ff827437bfc96d88732d6177b1ac5b5f
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/hatch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hatch

Gestor de proyectos Python moderno y extensible.
Vea también: `poetry`.
Más información: <https://hatch.pypa.io/latest/cli/reference/>.

- Crea un nuevo proyecto Hatch:

`hatch new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proyecto</span>

- Inicializa Hatch para un proyecto existente:

`hatch new --init`

- Construye un proyecto Hatch:

`hatch build`

- Elimina artefactos de construcción:

`hatch clean`

- Crea un entorno por defecto con las dependencias definidas en el archivo `pyproject.toml`:

`hatch env create`

- Muestra las dependencias del entorno en forma de tabla:

`hatch dep show table`
