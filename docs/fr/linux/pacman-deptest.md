---
layout: page
title: linux/pacman-deptest (français)
description: "Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas."
content_hash: 1017521d4ff3ba9fde15222ef7635b8886839bdf
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas.
Voir aussi: `pacman`.
Plus d'informations : <https://manned.org/pacman.8>.

- Affiche les noms des paquets qui ne sont pas installés dans la liste :

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1 paquet2 ...</span>

- Vérifie que le paquet installé a une version supérieure ou égale :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Vérifie qu'une version ultérieure du paquet est installée :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Affiche l'aide :

`pacman --deptest --help`
