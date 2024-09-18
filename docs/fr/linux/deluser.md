---
layout: page
title: linux/deluser (français)
description: "Supprime un utilisateur du système."
content_hash: ef9bfa0f7564884d3d3b525fa0461c8dc4fec8fc
last_modified_at: 2024-09-18
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
tldri18n_status: 2
---
# deluser

Supprime un utilisateur du système.
Plus d'informations : <https://manned.org/deluser>.

- Supprime un utilisateur :

`sudo deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et son répertoire "home" :

`sudo deluser --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et son répertoire "home", mais sauvegarde ses fichiers dans une archive `.tar.gz` dans le répertoire spécifié :

`sudo deluser --backup-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire/de/sauvegarde</span>` --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>

- Supprime un utilisateur et tous les fichiers qu'il possède :

`sudo deluser --remove-all-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_dutilisateur</span>
