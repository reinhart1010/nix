---
layout: page
title: common/drill (français)
description: "Effectue diverses requêtes DNS."
content_hash: 9ac83a7b7d89ecc66c4814442a62b0505a816467
last_modified_at: 2023-10-04
related_topics:
  - title: English version
    url: /en/common/drill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/drill.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># drill

Effectue diverses requêtes DNS.
Plus d'informations : <https://manned.org/drill>.

- Recherche des adresses IP(s) associées à un nom d'hôte (enregistrements A) :

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Recherche le(s) serveur(s) de messagerie associé(s) à un nom de domaine donné (enregistrement MX) :

`drill mx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Obtient tous les types d'enregistrements pour un nom de domaine donné :

`drill any `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Spécifie un autre serveur DNS à interroger :

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Effectue une recherche DNS inversée sur une adresse IP (enregistrement PTR) :

`drill -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Suit la traçabilité DNSSEC des serveurs racines jusqu'à un nom de domaine :

`drill -TD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Affiche le(s) enregistrement(s) DNSKEY d'un nom de domaine :

`drill -s dnskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
