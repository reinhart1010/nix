---
layout: page
title: common/git-pull (español)
description: "Obtiene rama de un repositorio remoto y lo fusiona con el repositorio local."
content_hash: 044456f386baef552c7415417f5301e3591b6689
last_modified_at: 2023-12-05
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
  - title: Indonesia version
    url: /id/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-pull.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pull

Obtiene rama de un repositorio remoto y lo fusiona con el repositorio local.
Más información: <https://git-scm.com/docs/git-pull>.

- Descarga cambios del repositorio remoto por defecto y lo fusiona:

`git pull`

- Descarga cambios del repositorio remoto por defecto y usa avance rápido (*fast forward*):

`git pull --rebase`

- Descarga cambios de un repositorio remoto y una rama específica para fusionarlos en HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>
