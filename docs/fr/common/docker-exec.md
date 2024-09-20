---
layout: page
title: common/docker-exec (français)
description: "Exécute une commande dans un conteneur déjà en cours d'exécution."
content_hash: 1111c4e87be86864f27fc7ad91bd8696e227c7c8
last_modified_at: 2024-09-20
related_topics:
  - title: Deutsch version
    url: /de/common/docker-exec.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-exec.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-exec.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-exec.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker exec

Exécute une commande dans un conteneur déjà en cours d'exécution.
Plus d'informations : <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Entrer dans un shell interactif dans un conteneur en cours d'exécution :

`docker exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Exécuter une commande en arrière-plan (détachée) dans un conteneur en cours d'exécution :

`docker exec --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Sélectionner le répertoire de travail pour une commande donnée à exécuter :

`docker exec --interactive --tty --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Exécuter une commande en arrière-plan sur un conteneur existant mais garder `stdin` ouvert :

`docker exec --interactive --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Définir une variable d'environnement dans une session Bash en cours d'exécution :

`docker exec --interactive --tty --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_d_environnement</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Exécuter une commande en tant qu'utilisateur spécifique :

`docker exec --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_conteneur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>
