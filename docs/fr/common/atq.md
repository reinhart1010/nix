---
layout: page
title: common/atq (français)
description: "Affiche les travaux programmés par la commande `at` ou `batch`."
content_hash: 7f0a651822dfa541dc184ce13265df586cfd4658
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># atq

Affiche les travaux programmés par la commande `at` ou `batch`.
Plus d'informations : <https://manned.org/atq>.

- Affiche les travaux programmés de l'utilisateur courant :

`atq`

- Affiche les travaux de la file nommé 'a' (les files ont des noms avec une seule lettre) :

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Affiche les travaux de tous les utilisateurs (lancé en tant que super-utilisateur) :

`sudo atq`
