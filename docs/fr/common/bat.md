---
layout: page
title: common/bat (français)
description: "Affiche et concatène le contenu d'un ou plusieurs fichiers."
content_hash: 3dba5cc52e8771a771201642291b7bbeb204ba31
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/bat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/bat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bat

Affiche et concatène le contenu d'un ou plusieurs fichiers.
Un clone de `cat` avec mise en valeur de la syntaxe et intégration avec Git.
Plus d'informations : <https://github.com/sharkdp/bat>.

- Affiche le contenu d'un fichier sur la sortie standard :

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Concatène le contenu de plusieurs fichiers vers le fichier de destination :

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_destination</span>

- Ajoute le contenu d'un ficher à la fin du fichier de destination :

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_destination</span>

- Numérote toutes les lignes affichées :

`bat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Affiche le contenu d'un fichier JSON sur la sortie standard avec mise en valeur de la syntaxe :

`bat --language json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.json</span>

- Affiche tous les langages pris en charge :

`bat --list-languages`
