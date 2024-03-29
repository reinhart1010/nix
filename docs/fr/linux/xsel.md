---
layout: page
title: linux/xsel (français)
description: "Outil de sélection et de manipulation du presse-papiers X11."
content_hash: 57eb4ebe660a2e027977c600553324fdbd24146d
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/xsel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsel

Outil de sélection et de manipulation du presse-papiers X11.
Plus d'informations : <https://manned.org/xsel>.

- Utilise la sortie d'une commande comme entrée du presse-papiers (équivalent de `Ctrl + C`) :

`echo 123 | xsel -ib`

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
