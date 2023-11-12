---
layout: page
title: common/git-rev-list (español)
description: "Muestra las revisiones (commits) en orden cronológico inverso."
content_hash: dbb4d3c46c09bbae6301dcf050cf3f118ab5d30c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-rev-list.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-list.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-list.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-list

Muestra las revisiones (commits) en orden cronológico inverso.
Más información: <https://git-scm.com/docs/git-rev-list>.

- Muestra todos los commits de la rama actual:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Imprime el último commit que cambió (agregó/editó/eliminó) un archivo específico en la rama actual:

`git rev-list -n 1 HEAD -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra los commits más recientes a partir de una fecha y una rama específica:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_rama</span>

- Muestra todos los commits fusionados en un commit específico:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Imprime el número de commits desde una etiqueta específica:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>`..HEAD --count`
