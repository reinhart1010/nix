---
layout: page
title: common/ack (français)
description: "Un outil de recherche comme grep, optimisé pour les développeurs."
content_hash: b4218d43e06887ca87542a2a13cebbb4e152c978
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ack

Un outil de recherche comme grep, optimisé pour les développeurs.
Regardez aussi : `rg`, qui est beaucoup plus rapide.
Plus d'informations : <https://beyondgrep.com/documentation>.

- Recherche des fichiers contenant une chaine de caractère ou une expression régulière dans le répertoire courant récursivement :

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Recherche pour un motif insensible à la casse :

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Recherche les lignes qui correspondent à un motif, affiche uniquement les textes correspondants et pas le reste de la ligne :

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Limite la recherche aux fichiers d'un certain type :

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Exlcus un certain type de fichier de la recherche :

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Compte le nombre total de correspondances :

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Affiche les noms et le nombre total de correspondances pour chaque fichiers :

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Affiche toutes les valeurs qui peuvent être utilisées avec `--type` :

`ack --help-types`
