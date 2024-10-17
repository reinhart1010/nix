---
layout: page
title: common/git-diff (español)
description: "Muestra los cambios en los archivos rastreados."
content_hash: 42e8899148b11713bd331a392a85207f76d2a762
last_modified_at: 2024-10-17
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
  - title: 한국어 version
    url: /ko/common/git-diff.html
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

Muestra los cambios en los archivos rastreados.
Más información: <https://git-scm.com/docs/git-diff>.

- Muestra cambios no preparados:

`git diff`

- Muestra todos los cambios no confirmados (incluyendo los preparados):

`git diff HEAD`

- Muestra sólo los cambios preparados (añadidos, pero aún no confirmados):

`git diff --staged`

- Muestra los cambios de todos los confirmados desde una fecha/hora dada (una expresión de fecha, por ejemplo "1 week 2 days" o una fecha ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Muestra estadísticas de diff, como archivos cambiados, histograma y total de inserciones/eliminaciones de líneas:

`git diff --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra un resumen de creaciones de archivos, renombramientos y cambios de modo desde una confirmación dada:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Compara un único archivo entre dos ramas o confirmaciones:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Compara distintos archivos de la rama actual con otra rama:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
