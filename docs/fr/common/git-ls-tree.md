---
layout: page
title: common/git-ls-tree (français)
description: "Lister le contenu d'un arbre."
content_hash: 830101c7eb03bd2c77d2cb50bc22b6dea5b0ea92
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-ls-tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-ls-tree.html
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

Lister le contenu d'un arbre.
Plus d'informations : <https://git-scm.com/docs/git-ls-tree>.

- Lister le contenu de l'arbre dans la branche :

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Lister le contenu de l'arbre dans le commit, récursif avec les sous-arbres :

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- Lister uniquement les noms de fichiers de l'arbre dans un commit :

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>
