---
layout: page
title: linux/resolvectl (français)
description: "Résout les noms de domaine, les adresses IPV4 et IPv6, les enregistrements de ressources DNS et les services."
content_hash: 726721a2c98f0d09a233767d4d4a4eaa99395e7f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/resolvectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/resolvectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# resolvectl

Résout les noms de domaine, les adresses IPV4 et IPv6, les enregistrements de ressources DNS et les services.
Inspecte et reconfigure le résolveur DNS.
Plus d'informations : <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Affiche les paramètres DNS :

`resolvectl status`

- Résout les adresses IPv4 et IPv6 pour un ou plusieurs domaines :

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domaine1 domaine2 ...</span>

- Récupère le domaine d'une IP spécifiée :

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adresse_ip</span>

- Vide tous les caches DNS locaux :

`resolvectl flush-caches`

- Affiche les statistiques DNS (transactions, cache et verdicts DNSSEC) :

`resolvectl statistics`

- Récupère un enregistrement MX du domaine :

`resolvectl --legend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MX</span>` query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domaine</span>

- Résout un enregistrement SRV, par exemple _xmpp-server._tcp gmail.com :

`resolvectl service _`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>`._`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocole</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Récupère une clé TLS :

`resolvectl tlsa tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>`:443`
