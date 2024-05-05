---
layout: page
title: common/ack (français)
description: "Un outil de recherche comme grep, optimisé pour les développeurs."
content_hash: 55aa195f181a26a3c35aa9fdcccceded5d299f1a
last_modified_at: 2024-05-05
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
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
tldri18n_status: 2
---
# ack

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

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Exlcus un certain type de fichier de la recherche :

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Compte le nombre total de correspondances :

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Affiche les noms et le nombre total de correspondances pour chaque fichiers :

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif_de_recherche</span>`"`

- Affiche toutes les valeurs qui peuvent être utilisées avec `--type` :

`ack --help-types`
