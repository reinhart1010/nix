---
layout: page
title: common/git-diff (español)
description: "Muestra los cambios de los archivos rastreados."
content_hash: d3b84252a60df9c2e4ed1b260eeacc8f0024cd39
last_modified_at: 2024-01-10
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

- Muestra los cambios sin marcar ni confirmación:

`git diff`

- Muestra todos los cambios sin confirmación, pero incluye los marcados:

`git diff HEAD`

- Muestra solo los cambios marcados pero que no tienen confirmación:

`git diff --staged`

- Muestra los cambios de todas las confirmaciones a partir de una fecha y/o tiempo específico (p. ej., `1 week 2 days` o una fecha ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Muestra solo los nombres de los archivos cambiados en una confirmación específica:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra un resumen de los cambios hecho en una confirmación (p. ej. permisos de un archivo):

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Compara un único archivo entre dos ramas o confirmaciones:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Compara diferentes archivos de la rama actual con otra rama:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>
