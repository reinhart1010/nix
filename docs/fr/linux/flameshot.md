---
layout: page
title: linux/flameshot (français)
description: "Outil de capture d'écran avec une interface graphique."
content_hash: d89953f6d86f54fa278eb7b4e3007bfb607bad0e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># flameshot

Outil de capture d'écran avec une interface graphique.
Ajoute du texte, des formes, des couleurs et envoie à imgur.
Plus d'informations : <https://flameshot.org>.

- Lancez Flameshot en mode graphique :

`flameshot launcher`

- Prenez une capture d'écran en cliquant et en faisant glisser :

`flameshot gui`

- Prenez une capture d'écran en plein écran :

`flameshot full`

- Définissez le chemin de sauvegarde :

`flameshot full --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Retardez la capture d'écran de N millisecondes et la sortie dans le presse-papiers :

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>` --clipboard`
