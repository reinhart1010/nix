---
layout: page
title: common/git-rev-parse (español)
description: "Muestra metadatos relativos a revisiones específicas."
content_hash: 562a25c0929da7aa774ccbf1807b943fdb5ee90a
last_modified_at: 2024-01-10
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

- Obtén el hash de la confirmación de una rama:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Obtén el nombre de la rama actual:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Obtén la ruta absoluta al directorio raíz:

`git rev-parse --show-toplevel`
