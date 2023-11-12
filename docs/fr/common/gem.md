---
layout: page
title: common/gem (français)
description: "Un gestionnaire de paquets pour le langage de programmation Ruby."
content_hash: 40fd10edb0c9363dc4742429dcb32571d064cfe9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/gem.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/gem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gem

Un gestionnaire de paquets pour le langage de programmation Ruby.
Plus d'informations : <https://guides.rubygems.org>.

- Recherche des gems distantes et affiche toutes les versions disponibles :

`gem search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_régulière</span>` --all`

- Installe la dernière version d'une gem :

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>

- Installe une version spécifique d'une gem :

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Installe la dernière version correspondante (SemVer) d'une gem :

`gem install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>` --version '~> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0</span>`'`

- Mise à jour d'une gem :

`gem update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>

- Liste toutes les gems locales :

`gem list`

- Désinstalle une gem :

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>

- Désinstalle une version spécifique d'une gem :

`gem uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_gem</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>
