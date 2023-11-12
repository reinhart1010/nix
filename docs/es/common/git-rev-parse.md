---
layout: page
title: common/git-rev-parse (español)
description: "Muestra metadatos relativos a revisiones específicas."
content_hash: 36c1e9dee9ad6bf7e1fe93063b987d04b5ee154a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-rev-parse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-parse.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-parse.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-parse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-parse

Muestra metadatos relativos a revisiones específicas.
Más información: <https://git-scm.com/docs/git-rev-parse>.

- Obtiene el hash del commit de una rama:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Obtiene el nombre de la rama actual:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Obtiene la ruta absoluta al directorio raíz:

`git rev-parse --show-toplevel`
