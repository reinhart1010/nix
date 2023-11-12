---
layout: page
title: common/git-describe (français)
description: "Créer un nom unique et lisible pour un objet à partir d'une référence disponible."
content_hash: a7a7cf8b0fe7dd119b210de0946973cd52b468da
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-describe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-describe.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git describe

Créer un nom unique et lisible pour un objet à partir d'une référence disponible.
Plus d'informations : <https://git-scm.com/docs/git-describe>.

- Créer un nom unique pour le commit courant (le nom contient le tag le plus récent, le nombre de commits additionnels, et l'empreinte abrégée du commit) :

`git describe`

- Créer un nom avec une empreinte de commit de 4 caractères :

`git describe --abbrev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Générer un nom avec le chemin complet du tag :

`git describe --all`

- Décrire un tag Git :

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.0.0</span>

- Créer un nom pour le dernier commit d'une branche donnée :

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_branche</span>
