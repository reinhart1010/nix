---
layout: page
title: common/git-merge (español)
description: "Fusiona ramas."
content_hash: f86833ed966d7a33335ceeae12219cc1f701fb8e
last_modified_at: 2024-01-13
related_topics:
  - title: English version
    url: /en/common/git-merge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-merge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-merge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-merge.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-merge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git merge

Fusiona ramas.
Más información: <https://git-scm.com/docs/git-merge>.

- Fusiona una rama con la rama actual:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Edita el mensaje de fusión:

`git merge --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Fusiona una rama y crea una confirmación para la fusión:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Cancela una fusión en caso de conflictos:

`git merge --abort`

- Fusiona usando una estrategia específica:

`git merge --strategy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">estrategia</span>` --strategy-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción_de_estrategia</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>
