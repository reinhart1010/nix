---
layout: page
title: linux/abbr (français)
description: "Gère les abréviations pour le shell Fish."
content_hash: bbef4e2de4e31d9f1a6c4f2d1ec858b0113aa685
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abbr

Gère les abréviations pour le shell Fish.
Les mots définis par l'utilisateur sont remplacés par des phrases plus longues après leur saisie.
Plus d'informations : <https://fishshell.com/docs/current/cmds/abbr.html>.

- Ajoute une nouvelle abréviation :

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_abrégé</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments_de_la_commande</span>

- Renomme une abréviation existante :

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_nom</span>

- Supprime une abréviation existante :

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_abrégé</span>

- Importe les abréviations définies sur un autre hôte via SSH :

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_hôte</span>` abbr --show | source`
