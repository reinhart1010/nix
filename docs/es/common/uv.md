---
layout: page
title: common/uv (español)
description: "Un rápido gestor de paquetes y proyectos Python."
content_hash: 516951750c136af9b37281e4aa4ed53e153c43db
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv

Un rápido gestor de paquetes y proyectos Python.
Algunos subcomandos como `tool` y `python` tienen su propia documentación de uso.
Más información: <https://docs.astral.sh/uv/reference/cli>.

- Crea un nuevo proyecto Python en el directorio actual:

`uv init`

- Crear un nuevo proyecto Python en la ruta especificada:

`uv init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Añade una nueva dependencia al proyecto:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina una dependencia del proyecto:

`uv remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Ejecuta un script en el entorno del proyecto:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.py</span>

- Ejecuta un comando en el entorno del proyecto:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Actualiza el entorno de un proyecto desde `pyproject.toml`:

`uv sync`

- Crea un archivo de bloqueo para las dependencias del proyecto:

`uv lock`
