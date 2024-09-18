---
layout: page
title: linux/apt-mark (français)
description: "Utilitaire permettant de modifier l'état des paquets installés."
content_hash: 9b8f6325f5df80d906d89773724c10fcd0393948
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Utilitaire permettant de modifier l'état des paquets installés.
Plus d'informations : <https://manned.org/apt-mark.8>.

- Marquer un paquet comme étant automatiquement installé :

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Maintenir un paquet à sa version actuelle et empêcher les mises à jour :

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Permettre une nouvelle mise à jour d'un paquet :

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Afficher les paquets installés manuellement :

`apt-mark showmanual`

- Afficher les paquets détenus qui ne sont pas mis à jour :

`apt-mark showhold`
