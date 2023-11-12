---
layout: page
title: common/grep (français)
description: "Recherche des motifs dans un texte."
content_hash: f817854f7474d7447cc3228b9cd23a1e8fe3ec07
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# grep

Recherche des motifs dans un texte.
Supporte des motifs simples et des expressions régulières.
Plus d'informations : <https://www.gnu.org/software/grep/manual/grep.html>.

- Recherche une chaîne de caractères précise :

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche en ignorant la casse :

`grep -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche récursivement (en ignorant les fichiers non-texte) dans le dossier courant une chaîne de caractères précise :

`grep -RI `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>` .`

- Utilise des expressions régulières étendues (supporte `?`, `+`, `{}`, `()` et `|`) :

`grep -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche 3 lignes de [C]ontexte, avant ([B]efore), ou [A]près chaque concordance :

`grep -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C|B|A</span>` 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`grep -Hn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Utilise l'entrée standard au lieu d'un fichier :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>

- Inverse le résultat pour exclure des chaînes de caractères spécifiques :

`grep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>
