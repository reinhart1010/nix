---
layout: page
title: common/git-lfs (français)
description: "Travailler dans un registre Git avec des fichiers volumineux."
content_hash: d4f4132a0bf6393df99fe75b6e91c2588101d1b3
related_topics:
  - title: English version
    url: /en/common/git-lfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-lfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-lfs.html
    icon: bi bi-globe
---
# git lfs

Travailler dans un registre Git avec des fichiers volumineux.
Plus d'informations : <https://git-lfs.github.com>.

- Initialise le Git LFS :

`git lfs install`

- Suivre des fichiers correspondant à un pattern :

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Changer l'URL du point de terminaison Git LFS (utile si le serveur LFS est séparé du serveur Git) :

`git config -f .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_endpoint_url</span>

- Lister les pattern de fichiers suivis :

`git lfs track`

- Lister les fichiers suivis ayant été commité :

`git lfs ls-files`

- Pousser tout les objets LFS vers le serveur distant :

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>

- Chercher tout les objets LFS :

`git lfs fetch`

- Charger tout les objets LFS :

`git lfs checkout`
