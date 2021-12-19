---
layout: page
title: linux/sysctl (français)
description: "Liste et modifie les variables d'exécution du noyau."
content_hash: 6e5da5f5ea21ca24239042ed282b6ffd2c6d648c
related_topics:
  - title: Deutsch version
    url: /de/linux/sysctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/sysctl.html
    icon: bi bi-globe
---
# sysctl

Liste et modifie les variables d'exécution du noyau.

- Affiche toutes les variables disponibles et leurs valeurs :

`sysctl -a`

- Définis une variable d'état modifiable du noyau :

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section.modifiable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>

- Obtiens les gestionnaires de fichiers (handlers) actuellement ouverts :

`sysctl fs.file-nr`

- Obtiens la limite de nombre de fichiers ouverts simultanément :

`sysctl fs.file-max`

- Applique les changements de `/etc/sysctl.conf` :

`sysctl -p`
