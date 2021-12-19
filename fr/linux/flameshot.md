---
layout: page
title: linux/flameshot (français)
description: "Outil de capture d'écran avec une interface graphique."
content_hash: d89953f6d86f54fa278eb7b4e3007bfb607bad0e
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flameshot.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/flameshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
