---
layout: page
title: linux/pacman-key (français)
description: "Script enrobeur pour GnuPG utilisé pour gérer le trousseau de clés de pacman."
content_hash: e956aa264910ed61943c92d8523387d02c3f5f8c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pacman-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

Script enrobeur pour GnuPG utilisé pour gérer le trousseau de clés de pacman.
Voir aussi: `pacman`.
Plus d'informations : <https://man.archlinux.org/man/pacman-key>.

- Initialise le trousseau de clés de pacman :

`sudo pacman-key --init`

- Ajoute les clés par défaut pour Arch Linux :

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- Liste les clés publiques du trousseau de clés :

`pacman-key --list-keys`

- Ajoute les clés contenues dans le fichier spécifié :

`sudo pacman-key --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Reçois une clé depuis un serveur de clés :

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nom|email</span>`"`

- Affiche l'empreinte d'une clé du trousseau de clés :

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nom|email</span>`"`

- Signe, localement, une clé du trousseau de clés :

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nom|email</span>`"`

- Supprime une clé :

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|nom|email</span>`"`
