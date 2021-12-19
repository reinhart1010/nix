---
layout: page
title: linux/xclip (français)
description: "Outil de manipulation de presse-papiers X11, semblable à `xsel`."
content_hash: 63bb15fd76776e6685dc485bbad10f87fd7f43e2
related_topics:
  - title: العربية version
    url: /ar/linux/xclip.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xclip.html
    icon: bi bi-globe
---
# xclip

Outil de manipulation de presse-papiers X11, semblable à `xsel`.
Gère les sélections primaires et secondaires de X, en plus du presse-papier système (`Ctrl + C`/`Ctrl + V`).

- Copie la sortie d'une commande vers la zone de sélection primaire de X11 (presse-papiers) :

`echo 123 | xclip`

- Copie la sortie d'une commande vers une zone de sélection de X11 donnée :

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- Copie le contenu d'un fichier vers le presse-papiers système, avec la notation courte :

`echo 123 | xclip -sel clip`

- Copie le contenu d'un fichier vers le presse-papiers système :

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_entrée.txt</span>

- Copie le contenu d'une image PNG vers le presse-papiers système (peut être collé dans d'autres programmes correctement) :

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_entrée.png</span>

- Colle le contenu de la zone de sélection de X11 à la console :

`xclip -o`

- Colle le contenu du presse-papier système à la console :

`xclip -o -sel clip`

- Colle le contenu du presse-papier système à un fichier :

`xclip -o -sel clip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_sortie.txt</span>
