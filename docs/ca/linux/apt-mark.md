---
layout: page
title: linux/apt-mark (català)
description: "Eina per canviar l'estat dels paquets instal·lats."
content_hash: c2272a4b439b0e3fda4b5d3eab922f3dc226b838
last_modified_at: 2023-11-12
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

Eina per canviar l'estat dels paquets instal·lats.
Més informació: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

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
