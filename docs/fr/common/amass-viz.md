---
layout: page
title: common/amass-viz (français)
description: "Visualise les informations recueillies dans graphique de réseau."
content_hash: 2a43080ed2e9b074d8abbc07b7f115c97063b0ea
related_topics:
  - title: English version
    url: /en/common/amass-viz.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass viz

Visualise les informations recueillies dans graphique de réseau.
Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Génère une visualisation D3.js basé sur la data de la base de données :

`amass viz -d3 -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>

- Génère un fichier DOT basé sur la data de la base de données :

`amass viz -dot -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>

- Génère un fichier GEXF basé sur la data de la base de données :

`amass viz -gexf -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>

- Génère un fichier JSON Graphistry basé sur la data de la base de données :

`amass viz -graphistry -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>

- Génère un fichier CSV Maltego basé sur la data de la base de données :

`amass viz -maltego -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>
