---
layout: page
title: common/git-rev-parse (français)
description: "Afficher les métadonnées liées à des révisions spécifiques."
content_hash: c79f05122d9c5bf42e9cb5865d18cebb27d3d072
related_topics:
  - title: English version
    url: /en/common/git-rev-parse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-parse.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-parse.html
    icon: bi bi-globe
---
# git rev-parse

Afficher les métadonnées liées à des révisions spécifiques.
Plus d'informations : <https://git-scm.com/docs/git-rev-parse>.

- Afficher l'empreinte du commit de la branche courante :

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Affiche le nom de la branche courante :

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Obtenir le chemin absolu du répertoire racine :

`git rev-parse --show-toplevel`
