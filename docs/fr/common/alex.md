---
layout: page
title: common/alex (français)
description: "Un outil qui corrige les phrases insensible et inconsidérée (en Anglais uniquement)."
content_hash: 1951d581e7152cc46c0cfac1e9854bbd5efaee60
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alex

Un outil qui corrige les phrases insensible et inconsidérée (en Anglais uniquement).
Il vous aide à trouver un genre, une polarité, une ethnie, un blasphème, ou autre inégalité en lisant un texte en anglais.
Plus d'informations : <https://github.com/get-alex/alex>.

- Analyse un texte depuis l'entrée standard :

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- Analyse tous les fichiers dans le dossier courant :

`alex`

- Analyse un fichier spécifique :

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichiertexte.md</span>

- Analyse tous les fichiers Markdown sauf `exemple.md` :

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.md</span>
