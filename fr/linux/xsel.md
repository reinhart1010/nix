---
layout: page
title: linux/xsel (français)
description: "Outil de sélection et de manipulation du presse-papiers X11."
content_hash: fd3dd5502b95d0240a5c111a05e96653e16d676c
related_topics:
  - title: English version
    url: /en/linux/xsel.html
    icon: bi bi-globe
---
# xsel

Outil de sélection et de manipulation du presse-papiers X11.

- Utilise la sortie d'une commande comme entrée du presse-papiers (équivalent de `Ctrl + C`) :

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123</span>` | xsel -ib`

- Utilise le contenu d'un fichier comme entrée du presse-papiers :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>` | xsel -ib`

- Affiche le contenu du presse-papiers dans le terminal (équivalent à `Ctrl + V`) :

`xsel -ob`

- Sortie du contenu du presse-papiers dans un fichier :

`xsel -ob > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Efface le presse-papiers :

`xsel -cb`

- Affiche le contenu de la sélection primaire X11 dans le terminal (équivalent à un clic du milieu de la souris) :

`xsel -op`
