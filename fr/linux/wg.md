---
layout: page
title: linux/wg (français)
description: "Gestion de la configuration des interfaces WireGuard."
content_hash: 892716564f1761b6b9d5a37ada9d2578b09a275b
related_topics:
  - title: English version
    url: /en/linux/wg.html
    icon: bi bi-globe
---
# wg

Gestion de la configuration des interfaces WireGuard.
Plus d'informations: <https://www.wireguard.com/quickstart/>.

- Vérifier l'état des interfaces actuellement actives :

`wg`

- Générer une clé privée :

`wg genkey`

- Générer une clé publique à partir d'une clé privée :

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>

- Générer une clé publique et privée :

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>

- Afficher la configuration actuelle d'une interface wireguard :

`wg showconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wg0</span>
