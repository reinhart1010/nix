---
layout: page
title: linux/apt-mark (català)
description: "Eina per canviar l'estat dels paquets instal·lats."
content_hash: 19b866d60ee836375f7a99be0194a510acc58266
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
  - title: français version
    url: /fr/linux/apt-mark.html
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

Eina per canviar l'estat dels paquets instal·lats.
Més Informació: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Marca un paquet com a instal·lat automàticament:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Manté un paquet en la seva versió actual i evita que s'actualitzi:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Permet que es pugui actualitzar de nou:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Mostra els paquets instal·lats manualment:

`apt-mark showmanual`

- Mostra els paquets mantinguts que no estàn actualitzats:

`apt-mark showhold`
