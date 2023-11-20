---
layout: page
title: common/atuin (français)
description: "Enregistre votre historique shell dans une base de donnée."
content_hash: 0074b248b96b892892531cea63be0016f68c4a4c
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/common/atuin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atuin

Enregistre votre historique shell dans une base de donnée.
Peut également synchroniser votre historique chiffré entre plusieurs machines.
Plus d'informations : <https://atuin.sh/docs/commands>.

- Installe atuin dans votre shell :

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- Importe l'historique du shell par défaut :

`atuin import auto`

- Recherche dans l'historique shell une commande spécifique :

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>

- Inscrire un compte sur le serveur de synchronisation par défaut :

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>

- Connexion au serveur de synchronisation par défaut :

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>

- Synchronise l'historique avec le serveur :

`atuin sync`
