---
layout: page
title: linux/deluser (français)
description: "Supprime un utilisateur du système."
content_hash: cf520e733ce70770e66d6d9e2fb5bc6b3849e4c3
related_topics:
  - title: English version
    url: /en/linux/deluser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/deluser.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/deluser.html
    icon: bi bi-globe
---
# deluser

Supprime un utilisateur du système.
Plus d'informations : <https://manpages.debian.org/latest/adduser/deluser.html>.

- Supprime un utilisateur :

`sudo deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et son répertoire "home" :

`sudo deluser --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et son répertoire "home", mais sauvegarde ses fichiers dans une archive `.tar.gz` dans le répertoire spécifié :

`sudo deluser --backup-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire/de/sauvegarde</span>` --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et tous les fichiers qu'il possède :

`sudo deluser --remove-all-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>
