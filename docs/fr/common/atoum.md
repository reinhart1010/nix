---
layout: page
title: common/atoum (français)
description: "Un framework de test unitaire pour PHP simple, moderne et intuitif."
content_hash: b2b5df89f656fbcc5d9d65ae41116f3bc1153341
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/atoum.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/atoum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atoum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atoum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atoum

Un framework de test unitaire pour PHP simple, moderne et intuitif.
Plus d'informations : <https://atoum.org>.

- Initialise un fichier de configuration :

`atoum --init`

- Lance les tests :

`atoum`

- Lance les tests avec un fichier de configuration donné :

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Lance un fichier de test spécifique :

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Lance les tests présent dans dossier donné :

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Lance tous les tests sous un certain namespace :

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Lance tous les tests avec un certain tag :

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Charge un fichier d'amorce avant de lancer les tests :

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
