---
layout: page
title: common/amass-db (français)
description: "Intéragie avec une base de données Amass."
content_hash: 85df4b769d891cefb6a93db2540004843a7263c3
related_topics:
  - title: English version
    url: /en/common/amass-db.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass db

Intéragie avec une base de données Amass.
Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Liste toutes les énumérations performées pas la base de données :

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_de_la_base_de_données</span>` -list`

- Affiche les résultats pour un index d'énumération et un nom de domaine spécifiés :

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_de_la_base_de_données</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_depuis_la liste</span>` -show`

- Liste tous les sous-domaines trouvés pour un domaine inclus dans une énumération :

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_de_la_base_de_données</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_depuis_la liste</span>` -names`

- Affiche un sommaire des sous-domaines inclus dans une énumération :

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier_de_la_base_de_données</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_depuis_la liste</span>` -summary`
