---
layout: page
title: common/git-rev-list (español)
description: "Muestra las revisiones (confirmaciones) en orden cronológico inverso."
content_hash: 5a5c08edbf523addc566fbdfd33e174fbf71d59c
last_modified_at: 2024-01-10
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

Muestra las revisiones (confirmaciones) en orden cronológico inverso.
Más información: <https://git-scm.com/docs/git-rev-list>.

- Muestra todas las confirmaciones de la rama actual:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Imprime la última confirmación que cambió (agregó/editó/eliminó) un archivo específico en la rama actual:

`git rev-list -n 1 HEAD -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra las confirmaciones más recientes a partir de una fecha y una rama específica:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_rama</span>

- Muestra todas las confirmaciones fusionadas en una confirmación específica:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Imprime el número de confirmaciones desde una etiqueta específica:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>`..HEAD --count`
