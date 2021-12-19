---
layout: page
title: linux/yay (français)
description: "Yet Another Yogurt : Un outil pour Arch Linux pour construire et installer des paquets depuis le Arch User Repository."
content_hash: ff70c0598335a17a2c470b15d13428249710fd49
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/yay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yay

Yet Another Yogurt : Un outil pour Arch Linux pour construire et installer des paquets depuis le Arch User Repository.
À regarder : `pacman`.
Plus d'informations : <https://github.com/Jguer/yay>.

- Recherche interactivement et installe des paquets depuis les dépôts et l'AUR :

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet|terme_recherche</span>

- Synchronise et met à jour tous les paquets depuis les dépôts et l'AUR :

`yay`

- Synchronise et met à jour seulement les paquets de l'AUR :

`yay -Sua`

- Installe un nouveau paquet depuis les dépôts et l'AUR :

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Recherche dans la base de données de paquets un mot clé depuis les dépôts et l'AUR :

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_clé</span>

- Montre des statistiques sur les paquets installés et la santé du système :

`yay -Ps`
