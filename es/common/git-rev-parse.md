---
layout: page
title: common/git-rev-parse (español)
description: "Muestra metados relativos a revisiones específicas."
content_hash: 6661f810ec06dc82ebc6d811bc706592cf368e40
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
---
# git rev-parse

Muestra metados relativos a revisiones específicas.
Más información: <https://git-scm.com/docs/git-rev-parse>.

- Obtiene el hash del commit de una rama:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Obtiene el nombre de la rama actual:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Obtiene la ruta absoluta al directorio raíz:

`git rev-parse --show-toplevel`
