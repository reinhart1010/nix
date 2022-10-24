---
layout: page
title: common/brew-cask (français)
description: "Outil en lignes de commande pour gérer les applications macOS distribuées sous forme de binaires."
content_hash: e8eb5b61b059b90d28292e70cf738f9fecd3ebff
related_topics:
  - title: Deutsch version
    url: /de/common/brew-cask.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-cask.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-cask.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew-cask.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew --cask

Outil en lignes de commande pour gérer les applications macOS distribuées sous forme de binaires.
Cette commande remplace `brew cask`, qui a été dépréciée en faveur de `brew --cask`.
Plus d'informations : <https://github.com/Homebrew/homebrew-cask>.

- Recherche une formule (c.a.d. un package) et/ou un casks (c.a.d une application native) :

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte</span>

- Installe un cask :

`brew install --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_cask</span>

- Liste les casks installés :

`brew list --cask`

- Liste les casks installés qui ont une nouvelle version disponible :

`brew outdated --cask`

- Met à jour le cask précisé (si aucun nom de cask n'est précisé, tous seront mis à jour) :

`brew upgrade --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_cask</span>

- Désinstalle un cask :

`brew uninstall --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_cask</span>

- Désinstalle un cask et supprime les paramètres et fichiers associés :

`brew zap --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_cask</span>

- Affiche les informations d'un cask en particulier :

`brew info --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_cask</span>
