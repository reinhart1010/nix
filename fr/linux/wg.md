---
layout: page
title: linux/wg (français)
description: "Gestion de la configuration des interfaces WireGuard."
content_hash: a0de109d0546478afcbc941867687eaada9efd22
related_topics:
  - title: English version
    url: /en/linux/wg.html
    icon: bi bi-globe
---
# wg

Gestion de la configuration des interfaces WireGuard.
Plus d'informations: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`wg`

- Générer une clé privée :

`wg genkey`

- Générer une clé publique à partir d'une clé privée :

`wg pubkey < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>

- Générer une clé publique et privée :

`wg genkey | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>` | wg pubkey > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_publique</span>
