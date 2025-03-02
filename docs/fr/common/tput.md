---
layout: page
title: common/tput (français)
description: "Accède et modifie les paramètres du terminal."
content_hash: 04c0a0d9abe670648b47f9f5ffeb92765eed4c3c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tput.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tput.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tput.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tput

Accède et modifie les paramètres du terminal.
Plus d'informations : <https://manned.org/tput>.

- Déplace le curseur à un endroit donné sur l'écran :

`tput cup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coordonnée_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coordonnée_x</span>

- Règle la couleur de l'avant-plan (af) ou de l'arrière-plan (ab) :

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setaf|setab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code_de_couleur_ANSI</span>

- Affiche le numéro de colonnes, de rangées, ou de couleurs :

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols|lines|colors</span>

- Active la sonnerie du terminal :

`tput bel`

- Réinitialise tous les attributs du terminal :

`tput sgr0`

- Active ou désactive le retour automatique à la ligne :

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>
