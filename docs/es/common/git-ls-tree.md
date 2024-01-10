---
layout: page
title: common/git-ls-tree (español)
description: "Muestra los contenidos de un objeto árbol."
content_hash: 08bd92325f8c85a46cbc330bfce8f408f5fb40b8
last_modified_at: 2024-01-10
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git ls-tree

Muestra los contenidos de un objeto árbol.
Más información: <https://git-scm.com/docs/git-ls-tree>.

- Muestra el contenido del árbol en una rama:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Muestra el contenido del árbol en una confirmación (recursivo en subárboles):

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_de_la_confirmación</span>

- Muestra solo los nombres de archivos del árbol en una confirmación:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash_de_la_confirmación</span>
