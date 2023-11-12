---
layout: page
title: common/brew (français)
description: "Gestionnaire de paquets pour macOS et Linux."
content_hash: dbfebd48bb07be5d772fc32e388e16f5229a0711
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

Gestionnaire de paquets pour macOS et Linux.
Plus d'informations : <https://docs.brew.sh/Manpage>.

- Installe la dernière version stable d'une formule ou d'un cask (ajouter `--devel` pour une version de développement):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formule</span>

- Liste toutes les formules et les casks installés :

`brew list`

- Met à jour une formule ou cask déjà installé (si rien n'est précisé, toutes les formules et tous les casks installés seront mis à jour) :

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formule</span>

- Récupère la dernière version d'Homebrew et toutes les formules et casks depuis le dépôt source d'Homebrew :

`brew update`

- Montre les formules et les casks disposants d'une nouvelle version :

`brew outdated`

- Recherche une formule (c.a.d. un package) et/ou un cask (c.a.d une application native) :

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte</span>

- Affiche les informations d'une formule ou d'un cask (version, chemin d'installation, dépendances, etc.) :

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formule</span>

- Vérifie que l'installation locale d'Homebrew n'a pas de problème :

`brew doctor`
