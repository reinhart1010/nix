---
layout: page
title: common/amass-enum (français)
description: "Trouve les sous-domaines d'un domaine."
content_hash: 53b17b94d96d4661307d1eb8a7e9d9c39724ae6d
related_topics:
  - title: English version
    url: /en/common/amass-enum.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass enum

Trouve les sous-domaines d'un domaine.
Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Trouve les sous-domaines d'un domaine passivement :

`amass enum -passive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>

- Trouve les sous-domaines d'un domaine et les verifie activement en essayant de résoudre les sous-domaines trouvés :

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Fait recherche par force brute pour les sous-domaines :

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>

- Sauvegarde les résultats vers un fichier texte :

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_domaine</span>

- Sauvegarde les résultats dans une base de données :

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la_base_de_données</span>
