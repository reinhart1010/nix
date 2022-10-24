---
layout: page
title: common/brew-bundle (français)
description: "Gestionnaire de paquets pour Homebrew, Homebrew Cask et le Mac App Store."
content_hash: 9dc39d61f2b786c18a8d2ee74acca5ba7f4bafc2
related_topics:
  - title: Deutsch version
    url: /de/common/brew-bundle.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-bundle.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew bundle

Gestionnaire de paquets pour Homebrew, Homebrew Cask et le Mac App Store.
Plus d'informations : <https://github.com/Homebrew/homebrew-bundle>.

- Installe tous les paquets listés dans le Brewfile situé dans le dossier courant :

`brew bundle`

- Installe tous les paquets listés dans le Brewfile situé au chemin spécifié :

`brew bundle --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Créé un Brewfile avec tous les paquets installés actuellement :

`brew bundle dump`

- Désinstalle tous les paquets non listés dans le Brewfile :

`brew bundle cleanup --force`

- Vérifie si il y a un ou plusieurs paquets à installer ou à mettre à jour depuis le Brewfile :

`brew bundle check`

- Affiche la liste de toutes les entrées dans un Brewfile :

`brew bundle list --all`
