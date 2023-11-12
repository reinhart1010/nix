---
layout: page
title: common/assimp (français)
description: "Client en ligne de commande pour l'Open Asset Import Library."
content_hash: 2599ee348636adc5f901c5ace8edee8030dea9ac
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/assimp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/assimp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/assimp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/assimp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# assimp

Client en ligne de commande pour l'Open Asset Import Library.
Supporte le chargement de plus de 40 formats de fichiers 3D, et exporte vers quelques formats 3D populaire.
Plus d'informations : <https://assimp-docs.readthedocs.io/>.

- Liste tous les formats d'import supportés :

`assimp listext`

- Liste tous les formats de sortie supportés :

`assimp listexport`

- Convertis un fichier vers un format de sortie supporté, avec les paramètres par défaut :

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_d_entrée.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie.obj</span>

- Convertis un fichier avec des paramètres personnalisés (le fichier dox_cmd.h dans le code source de assimp liste tous les paramètres disponible) :

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_d_entrée.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie.obj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paramètres</span>

- Affiche un sommaire du contenu d'un fichier 3D :

`assimp info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Liste toutes les sous-commandes supportées ("mots") :

`assimp help`

- Affiche l'aide d'un sous-commande (e.g les paramètres qui lui sont spécifique) :

`assimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sous_commande</span>` --help`
