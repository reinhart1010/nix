---
layout: page
title: common/git-merge (español)
description: "Fusiona ramas."
content_hash: cfdccb41f2c03ef5835956fe2dc16de41ce66a6d
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
---
# git merge

Fusiona ramas.
Más información: <https://git-scm.com/docs/git-merge>.

- Fusiona una rama con la rama actual:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Edita el mensaje de fusión:

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Fusiona una rama y crea un commit para la fusión:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Cancela una fusión en caso de conflictos:

`git merge --abort`
