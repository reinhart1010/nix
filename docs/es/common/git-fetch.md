---
layout: page
title: common/git-fetch (español)
description: "Descarga objetos y referencias de un repositorio remoto."
content_hash: b073857056c7fa6efe65b74812b0d80d0d6a7e18
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fetch

Descarga objetos y referencias de un repositorio remoto.
Más información: <https://git-scm.com/docs/git-fetch>.

- Recibe los últimos cambios del repositorio remoto upstream por defecto (si se ha establecido):

`git fetch`

- Recibe las ramas nuevas de un repositorio remoto upstream específico:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Recibe los últimos cambios de todos los repositorios remotos upstream:

`git fetch --all`

- Recibe también las etiquetas de un repositorio upstream:

`git fetch --tags`

- Elimina las referencias locales a ramas remotas que han sido eliminadas de upstream:

`git fetch --prune`
