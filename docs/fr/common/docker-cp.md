---
layout: page
title: common/docker-cp (français)
description: "Copier des fichiers ou des répertoires entre les systèmes de fichiers hôte et conteneur."
content_hash: fe87dd54f0c5953f582172fb147981bc25a10c17
last_modified_at: 2024-09-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker cp

Copier des fichiers ou des répertoires entre les systèmes de fichiers hôte et conteneur.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/cp/>.

- Copier un fichier ou un répertoire de l'hôte vers un conteneur :

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_fichier_ou_le_dossier_de_l_hote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_fichier_ou_le_dossier_de_conteneur</span>

- Copier un fichier ou un répertoire d'un conteneur vers l'hôte :

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_fichier_ou_le_dossier_de_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_fichier_ou_le_dossier_de_l_hote</span>

- Copier un fichier ou un répertoire de l'hôte vers un conteneur, en suivant les liens symboliques (copie les fichiers liés directement, pas les liens symboliques eux-mêmes) :

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_lien_symbolique_de_l_hote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le_fichier_ou_le_dossier_de_conteneur</span>
