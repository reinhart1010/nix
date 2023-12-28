---
layout: page
title: linux/wg (français)
description: "Gestion de la configuration des interfaces WireGuard."
content_hash: cabee91ade927913aac356d9ff81fee31fecf054
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/wg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wg

Gestion de la configuration des interfaces WireGuard.
Plus d'informations : <https://www.wireguard.com/quickstart/>.

- Vérifier l'état des interfaces actuellement actives :

`sudo wg`

- Générer une clé privée :

`wg genkey`

- Générer une clé publique à partir d'une clé privée :

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>

- Générer une clé publique et privée :

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>

- Afficher la configuration actuelle d'une interface wireguard :

`sudo wg showconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wg0</span>
