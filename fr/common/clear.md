---
layout: page
title: common/clear (français)
description: "Efface l'écran du terminal."
content_hash: 52b7c6a757d903dbe6c80a89f851f6c5b0ada7b4
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
---
# clear

Efface l'écran du terminal.
Plus d'informations : <https://manned.org/clear>.

- Effacer l'écran (identique à la séquence Contrôle-L sur une interface bash) :

`clear`

- Effacer l'écran mais conserve le tampon de défilement du terminal :

`clear -x`

- Indiquer le type de terminal à effacer (utilise par défaut la variable d'environnement `TERM`) :

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_de_terminal</span>

- Afficher la version de `ncurses` utilisée par `clear` :

`clear -V`
