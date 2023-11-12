---
layout: page
title: linux/iwctl (français)
description: "Un outil de ligne de commande pour gérer iwd."
content_hash: 24d47f0804ce62f159b56052929a4be3ceb7de96
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/iwctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iwctl

Un outil de ligne de commande pour gérer iwd.
Plus d'informations : <https://iwd.wiki.kernel.org/gettingstarted>.

- Lancer le mode interactif, dans ce mode vous pouvez entrer les commandes directement, avec de l'auto-complétion :

`iwctl`

- Avoir l'aide générale :

`iwctl --help`

- Afficher vos stations wifi :

`iwctl station list`

- Lancer la recherche de réseaux avec une station :

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` scan`

- Afficher les réseaux trouvés par une station :

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` get-networks`

- Se connecter à un réseau avec une station, si des informations de connexion sont nécessaires elles seront demandées :

`iwctl station `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">station</span>` connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_réseau</span>
