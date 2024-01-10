---
layout: page
title: common/git-reset (español)
description: "Deshaz confirmaciones o desmarca cambios mediante el restablecimiento del actual HEAD de Git al estado especificado."
content_hash: ad5d5e85287027e2c832b66da5fd39385bb6ac73
last_modified_at: 2024-01-10
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

Deshaz confirmaciones o desmarca cambios mediante el restablecimiento del actual HEAD de Git al estado especificado.
Si se pasa una ruta, funciona como "desmarcar", si se pasa el hash de una confirmación o una rama, funciona como "deshacer" la confirmación.
Más información: <https://git-scm.com/docs/git-reset>.

- Desmarca todo:

`git reset`

- Desmarca un archivo o archivos específicos:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_archivos</span>

- Interactivamente desmarca partes de un archivo:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Deshaz la última confirmación, manteniendo sus cambios, y cualquier otro cambio sin confirmación, en el sistema de archivos:

`git reset HEAD~`

- Deshaz las últimas dos confirmaciones al añadir sus cambios al índice (p. ej. marcado para confirmación):

`git reset --soft HEAD~2`

- Descarta cualquier cambio sin confirmación, marcado o no (se puede `git checkout` solo para los cambios sin marcar):

`git reset --hard`

- Restablece el repositorio a una confirmación específica y descarta a partir de esta los cambios con y sin confirmación, y los marcados:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>
