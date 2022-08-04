---
layout: page
title: common/git-pull (español)
description: "Obtener rama de un repositorio remoto y fusionarlo con el repositorio local."
content_hash: d4e75e97b4d7d2841457524b522f085b5bceaa44
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
---
# git pull

Obtener rama de un repositorio remoto y fusionarlo con el repositorio local.
Más información: <https://git-scm.com/docs/git-pull>.

- Descargar cambios del repositorio remoto por defecto y fusionarlo:

`git pull`

- Descargar cambios del repositorio remoto por defecto y usar avance rápido (*fast forward*):

`git pull --rebase`

- Descargar cambios de un repositorio remoto y una rama específica para fusionarlos en HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>
