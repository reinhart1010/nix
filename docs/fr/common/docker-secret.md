---
layout: page
title: common/docker-secret (français)
description: "Gérer les secrets de Docker swarm."
content_hash: ed2c3b465b9a588b9d9a7fd342a41164dbf9e078
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-secret.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker secret

Gérer les secrets de Docker swarm.
Plus d'informations : <https://docs.docker.com/engine/reference/commandline/secret/>.

- Créer un nouveau secret depuis l'entrée standard :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_secret</span>` -`

- Créer un nouveau secret depuis un fichier :

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_secret</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Lister tous les secrets :

`docker secret ls`

- Afficher des informations détaillées sur un ou plusieurs secrets dans un format humain :

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_secret1 nom_du_secret2 ...</span>

- Supprimer un ou plusieurs secrets :

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_secret1 nom_du_secret2 ...</span>
