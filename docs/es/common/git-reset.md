---
layout: page
title: common/git-reset (español)
description: "Deshace commits o desmarca cambios mediante el reseteo del actual HEAD de Git al estado especificado."
content_hash: dd122793cd00ae58f3537a24c44d3495456dbc95
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-reset.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

Deshace commits o desmarca cambios mediante el reseteo del actual HEAD de Git al estado especificado.
Si se pasa una ruta, funciona como "desmarcar", si se pasa el hash de un commit o una rama, funciona como "deshacer" el commit.
Más información: <https://git-scm.com/docs/git-reset>.

- Desmarcar todo:

`git reset`

- Desmarcar un archivo o archivos específicos:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_archivos</span>

- Interactivamente desmarca partes de un archivo:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Deshace el último commit, manteniendo sus cambios,y cualquier otro cambios sin commit,en el sistema de archivo:

`git reset HEAD~`

- Deshace los últimos dos commits al añadir sus cambios al índice (por ej., marcado para commit):

`git reset --soft HEAD~2`

- Descartar cualquier cambio sin commit, marcado o no (se puede `git checkout` solo para los cambios sin marcar):

`git reset --hard`

- Resetea el repositorio a un commit específico y descarta a partir de este los cambios con y sin commit, y los marcados:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
