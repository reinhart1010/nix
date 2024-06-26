---
layout: page
title: common/git-lfs (français)
description: "Travailler dans un registre Git avec des fichiers volumineux."
content_hash: 69521f5b68eb0da9145cc55d38897622bab5b84e
last_modified_at: 2024-05-23
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
  - title: Türkçe version
    url: /tr/common/git-lfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git lfs

Travailler dans un registre Git avec des fichiers volumineux.
Plus d'informations : <https://git-lfs.com>.

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
