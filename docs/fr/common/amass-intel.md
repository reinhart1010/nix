---
layout: page
title: common/amass-intel (français)
description: "Collecte des renseignements open source sur une organisation comme les noms de domaines racine et les ASNs."
content_hash: 9128122d382466f0d75bb4b4e5101e19bcfd7dfc
related_topics:
  - title: English version
    url: /en/common/amass-intel.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass intel

Collecte des renseignements open source sur une organisation comme les noms de domaines racine et les ASNs.
Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Recherche les domaines racines inclus dans une plage d'adresse IP :

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Utilise les méthodes de reconnaissance active :

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Recherche les noms de domaines racines reliés à un domaine :

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>

- Recherche les ASNs qui correspondent à une organisation :

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_organisation</span>

- Recherche les domaines racines qui correspondent à un ASN :

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- Sauvegarde les résultats dans un fichier texte :

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>
