---
layout: page
title: linux/pacman-deptest (français)
description: "Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas."
content_hash: 00f8f130a8d8bf7b2fafe3385ed447e8a7b33de5
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
---
# pacman --deptest

Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas.
Voir aussi: `pacman`.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Affiche les noms des paquets qui ne sont pas installés dans la liste :

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet2</span>

- Vérifie que le paquet installé a une version supérieure ou égale :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Vérifie qu'une version ultérieure du paquet est installée :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Affiche l'aide :

`pacman --deptest --help`
