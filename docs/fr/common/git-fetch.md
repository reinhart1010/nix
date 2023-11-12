---
layout: page
title: common/git-fetch (français)
description: "Cherche les objets et références depuis un dépôt distant."
content_hash: 65d34e10f4c43236313e79b4c26395523940822f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fetch

Cherche les objets et références depuis un dépôt distant.
Plus d'informations : <https://git-scm.com/docs/git-fetch>.

- Cherche les dernières modifications du référentiel amont distant par défaut (si configuré) :

`git fetch`

- Cherche les nouvelles branches depuis un registre distant :

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>

- Cherche les nouvelles branches depuis tous les registres distants :

`git fetch --all`

- Recherche également les tags depuis le registre courant :

`git fetch --tags`

- Supprime les références locales de branches ayant été supprimés du registre distant :

`git fetch --prune`
