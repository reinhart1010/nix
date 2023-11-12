---
layout: page
title: common/git-branch (español)
description: "Comando Git principal para trabajar con ramas."
content_hash: dde24995f639fd92491554027e214702a6d33019
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git branch

Comando Git principal para trabajar con ramas.
Más información: <https://git-scm.com/docs/git-branch>.

- Muestra las ramas locales. La rama actual está resaltada por `*`:

`git branch`

- Muestra todas las ramas (locales y remotas):

`git branch -a`

- Muestra el nombre de la rama actual:

`git branch --show-current`

- Crea una nueva rama basada en el commit actual:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea una nueva rama basada en un commit específico:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_del_commit</span>

- Renombra una rama (no debe haber sido fusionada para hacer esto):

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiguo_nombre_de_la_rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre_de_la_rama</span>

- Borra una rama local (no debe haber sido fusionada para hacer esto):

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Borra una rama remota:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama_remota</span>
