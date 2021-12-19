---
layout: page
title: common/git-instaweb (français)
description: "Outil pour le lancement d'un serveur gitweb."
content_hash: f8ae8f0fde7686d312b85bb258577702b2a5cb4e
related_topics:
  - title: English version
    url: /en/common/git-instaweb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-instaweb.html
    icon: bi bi-globe
---
# git instaweb

Outil pour le lancement d'un serveur gitweb.
Plus d'informations : <https://git-scm.com/docs/git-instaweb>.

- Démarre un serveur gitweb depuis le dépôt (`repository`) courant :

`git instaweb --start`

- Écoute uniquement sur le port localhost :

`git instaweb --start --local`

- Écoute sur un port spécifique :

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Utiliser un daemon http spécifique :

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- Lancer en même temps qu'un navigateur web :

`git instaweb --start --browser`

- Stoppe le serveur :

`git instaweb --stop`

- Redémarre le serveur :

`git instaweb --restart`
