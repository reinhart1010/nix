---
layout: page
title: common/vegeta (français)
description: "Un utilitaire de ligne de commande et une bibliothèque pour les tests de charge HTTP."
content_hash: 6c224dde9c122dcfd95aff36d67fa53273dd163e
related_topics:
  - title: English version
    url: /en/common/vegeta.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># vegeta

Un utilitaire de ligne de commande et une bibliothèque pour les tests de charge HTTP.
Voir aussi `ab`.
Plus d'informations : <https://github.com/tsenart/vegeta>.

- Lancer une attaque d'une durée de 30 secondes :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://exemple.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- Lancez une attaque sur un serveur avec un certificat HTTPS auto-signé :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://exemple.com</span>`" | vegeta attack -insecure -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- Lancer une attaque avec un taux de 10 demandes par seconde :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://exemple.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Lancer une attaque et afficher un rapport :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://exemple.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta report`

- Lancer une attaque et reporter les résultats sur un graphique (latence en fonction du temps) :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://exemple.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/au/results.html</span>

- Lancer une attaque contre plusieurs URL à partir d'un fichier :

`vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -targets=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requetes.txt</span>` | vegeta report`
