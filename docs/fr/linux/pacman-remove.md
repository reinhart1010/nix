---
layout: page
title: linux/pacman-remove (français)
description: "Supprimes des paquets."
content_hash: 80834c5c50e31009002332dc4323b19ea1f91e31
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

Supprimes des paquets.
Voir aussi: `pacman`.
Plus d'informations : <https://manned.org/pacman.8>.

- Supprime un paquet et ses dépendances :

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Supprime un paquet, ses dépendances et ses fichiers de configuration :

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Supprime un paquet silencieusement :

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Supprime les paquets orphelins (installés en tant que dépendance mais requis par aucun paquet installé) :

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Supprime un paquet et les paquets qui en dépendent :

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Affiche les paquets qui seraient affectés par la commande sans agir :

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Affiche l'aide :

`pacman --remove --help`
