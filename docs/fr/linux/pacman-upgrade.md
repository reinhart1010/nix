---
layout: page
title: linux/pacman-upgrade (français)
description: "Mets à jour ou ajoute des paquets au système."
content_hash: 3540cc6cb926b5112f45f84d43497d408366f4b0
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Mets à jour ou ajoute des paquets au système.
Voir aussi: `pacman`.
Plus d'informations : <https://manned.org/pacman.8>.

- Installe un ou des paquets depuis le système de fichiers :

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet2.pkg.tar.zst</span>

- Installe un paquet silencieusement :

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Ecris par dessus les fichiers en conflit pendant l'installation du paquet :

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Installe un paquet sans vérifier les dépendances :

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Affiche ce qui se passerait si la commande était exécutée mais sans agir :

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/paquet.pkg.tar.zst</span>

- Affiche l'aide :

`pacman --upgrade --help`
