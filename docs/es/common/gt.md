---
layout: page
title: common/gt (español)
description: "Crea y gestiona secuencias de cambios de código dependientes (stacks) para Git y GitHub."
content_hash: aa78ddf8ce52ab6f73ee8aa2418e9aedaa210cf7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gt

Crea y gestiona secuencias de cambios de código dependientes (stacks) para Git y GitHub.
Más información: <https://graphite.dev/docs/get-started>.

- Inicializa `gt` para el repositorio en el directorio actual:

`gt init`

- Crea una nueva rama apilada sobre la rama actual y confirmar los cambios por etapas:

`gt create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_rama</span>

- Crea un nuevo commit y arreglar las ramas apiladas:

`gt modify -cam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_de_commit</span>

- Fuerza el push de todas las ramas de la pila actual a GitHub y crea o actualiza PRs:

`gt stack submit`

- Comprueba una rama diferente (solicita el modo interactivo cuando se omite el nombre de la rama):

`gt co `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_rama</span>

- Sincroniza la pila con la versión remota (también elimina las ramas fusionadas):

`gt sync`

- Registra todas las pilas rastreadas:

`gt log short`

- Muestra la ayuda de un subcomando específico:

`gt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`
