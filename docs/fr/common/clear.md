---
layout: page
title: common/clear (français)
description: "Efface l'écran du terminal."
content_hash: 22581236f1ecf8e4ea895590903aa1b2a1ca6b7c
last_modified_at: 2024-03-10
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

Efface l'écran du terminal.
Plus d'informations : <https://manned.org/clear>.

- Effacer l'écran (identique à la séquence Contrôle-L sur une interface Bash) :

`clear`

- Effacer l'écran mais conserve le tampon de défilement du terminal :

`clear -x`

- Indiquer le type de terminal à effacer (utilise par défaut la variable d'environnement `TERM`) :

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_de_terminal</span>

- Afficher la version de `ncurses` utilisée par `clear` :

`clear -V`
