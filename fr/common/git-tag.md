---
layout: page
title: common/git-tag (français)
description: "Créer, lister, vérifier et supprimer des tags."
content_hash: ebd3ad0db76fa8971c98e91766e08e83e5ad1810
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
---
# git tag

Créer, lister, vérifier et supprimer des tags.
Un tag est une référence statique vers un commit.
Plus d'informations : <https://git-scm.com/docs/git-tag>.

- Lister tout les tags :

`git tag`

- Créer un tag avec le nom donné pointant vers le commit actuel :

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_etiquette</span>

- Créer un tag avec le nom donné pointant vers un commit spécifié :

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_etiquette</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Créer un tag annoté avec le message spécifié :

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_etiquette</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_d_etiquette</span>

- Supprimer le tag avec le nom spécifié :

`git tag -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_etiquette</span>

- Mettre à jour les tags depuis l'origine :

`git fetch --tags`

- Liste toutes les tags dont les ancêtres incluent un commit donné :

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
