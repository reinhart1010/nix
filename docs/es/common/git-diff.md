---
layout: page
title: common/git-diff (español)
description: "Muestra los cambios de los archivos rastreados."
content_hash: 42e27e2ffaf0c8f98687da18422c79904ae7ff49
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff

Muestra los cambios de los archivos rastreados.
Más información: <https://git-scm.com/docs/git-diff>.

- Muestra los cambios sin marcar ni commit:

`git diff`

- Muestra todos los cambios sin commit, pero incluye los marcados:

`git diff HEAD`

- Muestra solo los cambios marcados pero que no tienen commit:

`git diff --staged`

- Muestra los cambios de todos los commits a partir de una fecha/tiempo específico (una expresión de fecha, por ej., "1 week 2 days" o una fecha ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}`

- Muestra solo los nombres de los archivos cambiados con un commit específico:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Muestra un resumen de la creación, renombre y modos de cambio con un commit específico:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compara un único archivo entre dos ramas o commits:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Compara diferentes archivos de la rama actual con otra rama:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>
