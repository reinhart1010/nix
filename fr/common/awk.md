---
layout: page
title: common/awk (français)
description: "Langage de programmation polyvalent pour travailler sur des fichiers."
content_hash: 57cb230ef6cd88998c887ef5d83eadf789b7bed4
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
---
# awk

Langage de programmation polyvalent pour travailler sur des fichiers.
Plus d'informations : <https://github.com/onetrueawk/awk>.

- Affiche la cinquième colonne (ou le champ) dans un fichier qui utilise des espaces comme séparateur :

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Affiche la deuxième colonne dans des lignes contenant "quelque-chose" dans un fichier qui utilise des espaces comme séparateur :

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelque-chose</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Affiche la dernière colonne de chaque ligne d'un fichier en utilisant une virgule (au lieu des espaces) comme séparateur :

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Additionne les valeurs de la première colonne des lignes d'un fichier et affiche le total :

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Additionne les valeurs de la première colonne des lignes d'un fichier et affiche ces valeurs puis affiche le total :

`awk '{s+=$1; print $1} END {print "--------"; print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Affiche une ligne sur trois en partant de la première ligne :

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_fichier</span>

- Affiche les lignes dont la valeur de la colonne 10 vaut la valeur recherchée :

`awk '($10 == valeur)'`

- Affiche les lignes dont la valeur de la colonne 10 est comprise entre un min et un max :

`awk '($10 >= valeur_min && $10 <= valeur_max)'`
