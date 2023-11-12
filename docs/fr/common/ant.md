---
layout: page
title: common/ant (français)
description: "Apache Ant."
content_hash: 517a9870767dee6f8eeda8afad55dd9058fc315c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant.
Outil pour construire et gérer les projets basés sur du Java.
Plus d'informations : <https://ant.apache.org>.

- Construit un projet avec le fichier de construction `build.xml` :

`ant`

- Construit un projet en utilisant un autre fichier que `build.xml` :

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_construction.xml</span>

- Affiche les informations sur les cibles possibles pour ce projet :

`ant -p`

- Affiche les informations de débogage :

`ant -d`

- Exécute toutes les cibles qui ne dépendent pas d'une ou plusieurs cibles en erreur :

`ant -k`
