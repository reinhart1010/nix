---
layout: page
title: common/tr (français)
description: "Convertisseur de caractères : exécute des remplacements basés sur des caractères uniques et des jeux de caractères."
content_hash: 80ac798bea4cf17f87084f84ae901400ec4ca7bc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tr

Convertisseur de caractères : exécute des remplacements basés sur des caractères uniques et des jeux de caractères.
Plus d'informations : <https://www.gnu.org/software/coreutils/tr>.

- Remplace toutes les occurrences d'un caractère dans un fichier, et affiche le résultat :

`tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractère_recherché</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractère_remplacé</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Remplace toutes les occurrences d'un caractère dans la sortie d'une autre commande :

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte</span>` | tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractère_recherché</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractère_remplacé</span>

- Fais correspondre chaque caractère du premier ensemble au caractère correspondant du second ensemble :

`tr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abcd</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jkmn</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Supprime toutes les occurrences de l'ensemble de caractères spécifié dans l'entrée :

`tr -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractères_en_entrée</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Comprime une série de caractères identiques en un seul caractère :

`tr -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caractères_en_entrée</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Traduis le contenu d'un fichier en majuscules :

`tr "[:lower:]" "[:upper:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Supprime les caractères non imprimables d'un fichier :

`tr -cd "[:print:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>
