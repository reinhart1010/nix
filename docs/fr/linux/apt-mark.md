---
layout: page
title: linux/apt-mark (français)
description: "Utilitaire permettant de modifier l'état des paquets installés."
content_hash: fa92e26ca6130db5c7da058c9f2a36f69fe15fe3
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
---
# apt-mark

Utilitaire permettant de modifier l'état des paquets installés.
Plus d'informations : <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

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
