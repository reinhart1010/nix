---
layout: page
title: linux/apt-file (català)
description: "Busca arxius en paquets APT, incloent els que encara no s'han instal·lat."
content_hash: a8038f8cc1bd5ffc4630a8cb862a62d2f5fff308
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-file.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-file.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-file.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-file

Busca arxius en paquets APT, incloent els que encara no s'han instal·lat.
Més informació: <https://manned.org/apt-file.1>.

- Actualita les metadades de la base de dades:

`sudo apt update`

- Busca paquets que continguin l'arxiu o ruta especificada:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/arxiu</span>

- Mostra el contingut del paquet especificat:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_paquet</span>

- Busca paquets que igualin l'expressió regular donada en `patró`:

`apt-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search|find</span>` --regexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressió_regular</span>
