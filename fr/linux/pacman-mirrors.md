---
layout: page
title: linux/pacman-mirrors (français)
description: "Génère une liste de miroirs pour pacman sur Manjaro Linux."
content_hash: 199c2f976d484c4949e58acf341f6054750f6fe9
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
---
# pacman-mirrors

Génère une liste de miroirs pour pacman sur Manjaro Linux.
Tout appel à pacman-mirrors demande de synchroniser les bases de données et de mettre à jour le système en exécutant `sudo pacman -Syyu` en suivant.
Plus d'informations : <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Génère une liste de miroirs avec les réglages par défaut :

`sudo pacman-mirrors --fasttrack`

- Obtiens le statut des miroirs actuels :

`pacman-mirrors --status`

- Affiche la branche courante :

`pacman-mirrors --get-branch`

- Utilise une branche différente :

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- Génère une liste de miroirs se trouvant dans le pays associé à l'adresse IP :

`sudo pacman-mirrors --geoip`
