---
layout: page
title: common/git-gc (français)
description: "Optimise le dépôt local git en nettoyant les fichiers inutiles."
content_hash: 26c644c92f6590794fea8412ec6ef59cf1f5ddc0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-gc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-gc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-gc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-gc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-gc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git gc

Optimise le dépôt local git en nettoyant les fichiers inutiles.
Plus d'informations : <https://git-scm.com/docs/git-gc>.

- Optimise le dépôt :

`git gc`

- Optimise le dépôt plus agressivement, plus long :

`git gc --aggressive`

- Afficher les objets à supprimer :

`git gc --no-prune`

- Supprime tout les objets trouvés sans les afficher sur la sortie standard :

`git gc --quiet`

- Afficher le manuel :

`git gc --help`
