---
layout: page
title: common/bundle (français)
description: "Gestionnaire de dépendances pour le langage de programmation Ruby."
content_hash: 4d218f96d227ab476f87247eb71fddc23d4a3e7d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundle

Gestionnaire de dépendances pour le langage de programmation Ruby.
Plus d'informations : <https://bundler.io/man/bundle.1.html>.

- Installe toutes les gems définies dans le `Gemfile` attendu dans le répertoire de travail :

`bundle install`

- Exécute une commande dans le contexte du bundle actuel :

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Mets à jour toutes les gems selon les règles définies dans le `Gemfile` et régénére le fichier `Gemfile.lock` :

`bundle update`

- Mets à jour une ou plusieurs gem(s) spécifique(s) définie(s) dans le `Gemfile` :

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_gem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_gem</span>

- Mets à jour une ou plusieurs gem(s) spécifique(s) définie(s) dans le `Gemfile` mais seulement vers la prochaine version de patch :

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_gem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_gem</span>

- Mets à jour toutes les gem(s) du groupe donné dans le `Gemfile` :

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_groupe</span>

- Liste les gem(s) installée(s) dans le `Gemfile` avec les nouvelles versions disponibles :

`bundle outdated`

- Crée un nouveau squelette de gem :

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_gem</span>
