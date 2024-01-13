---
layout: page
title: common/git-ls-tree (español)
description: "Muestra los contenidos de un objeto árbol."
content_hash: 8b5d52fae84cd95cf04578681c2f0f7dbdf9e4b5
last_modified_at: 2024-01-13
related_topics:
  - title: English version
    url: /en/common/git-ls-tree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-tree

Muestra los contenidos de un objeto árbol.
Más información: <https://git-scm.com/docs/git-ls-tree>.

- Lista el contenido del árbol en una rama:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Lista el contenido del árbol en una confirmación (recursivo en subárboles):

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_de_la_confirmación</span>

- Lista solo los nombres de archivos del árbol en una confirmación:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_de_la_confirmación</span>

- Lista el nombre de los archivos en la rama actual en forma de árbol (Nota: la opción `--fromfile` no está disponible en el comando `tree` de Windows):

`git ls-tree -r --name-only HEAD | tree --fromfile`
