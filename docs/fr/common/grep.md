---
layout: page
title: common/grep (français)
description: "Recherche des motifs dans un texte."
content_hash: 0cd25dc846a56af1ff03654fc5dadb3cff1ad43e
last_modified_at: 2024-01-15
related_topics:
  - title: dansk version
    url: /da/common/grep.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/grep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

Recherche des motifs dans un texte.
Supporte des motifs simples et des expressions régulières.
Plus d'informations : <https://www.gnu.org/software/grep/manual/grep.html>.

- Recherche une chaîne de caractères précise :

`grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche en ignorant la casse :

`grep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche récursivement (en ignorant les fichiers non-texte) dans le dossier courant une chaîne de caractères précise :

`grep --recursive --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" .`

- Utilise des expressions régulières étendues (supporte `?`, `+`, `{}`, `()` et `|`) :

`grep --extended-regexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche 3 lignes de [C]ontexte, avant ([B]efore), ou [A]près chaque concordance :

`grep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`grep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Utilise l'entrée standard au lieu d'un fichier :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` | grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`"`
