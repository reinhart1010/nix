---
layout: page
title: common/git-worktree (español)
description: "Gestiona múltiples árboles de trabajo adjuntos al mismo repositorio."
content_hash: 6555ad2b043217076acc4135d27dbe5b9d72dd92
related_topics:
  - title: English version
    url: /en/common/git-worktree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-worktree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-worktree.html
    icon: bi bi-globe
---
# git worktree

Gestiona múltiples árboles de trabajo adjuntos al mismo repositorio.
Más información: <https://git-scm.com/docs/git-worktree>.

- Crea un nuevo directorio con la rama específicada y se cambia él:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>

- Crea un nuevo directorio con un nueva rama y se cambia a él:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_nueva</span>

- Muestra todos los directorios de trabajo adjuntos a este repositorio:

`git worktree list`

- Elimina un árbol de trabajo (después de eliminar el directorio del árbol de trabajo):

`git worktree prune`
