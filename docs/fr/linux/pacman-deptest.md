---
layout: page
title: linux/pacman-deptest (français)
description: "Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas."
content_hash: 7f13efeb5c6e6bc6416f8f0f3bf1b5b3658428e8
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
---
# pacman --deptest

Vérifie la satisfaction des dépendances et renvoie celles qui ne le sont pas.
Plus d'informations : <https://man.archlinux.org/man/pacman.8>.

- Affiche les noms des paquets qui ne sont pas installés dans la liste :

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet2</span>

- Vérifie que le paquet installé a une version supérieure ou égale :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Vérifie qu'une version ultérieure du paquet est installée :

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Affiche l'aide :

`pacman --deptest --help`
