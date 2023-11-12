---
layout: page
title: linux/apt-get (català)
description: "Eina de gestió de paquets per a distribucions basades en Debian."
content_hash: ce0fc33be8010f92ca001d238d0cf5e214082fc2
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Eina de gestió de paquets per a distribucions basades en Debian.
Busca paquets utilizant `apt-cache`.
Més informació: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Actualitza la llista de paquets i versions disponibles (es recomana executar aquest comandament abans que qualsevol altre `apt-get`):

`apt-get update`

- Instala un paquet o l'actualitza a l'última versió disponible:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Elimina un paquet:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Elimina un paquet i els seus arxius de configuració:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Actualitza tots els paquets instal·lats a les noves versions disponibles:

`apt-get upgrade`

- Neteja el repositori local - eliminant fitxers de paquet (`.deb`) de descàrregues interrompudes que ja no es poden descarregar:

`apt-get autoclean`

- Elimina tots els paquets inneccessaris:

`apt-get autoremove`

- Actualitza paquets instal·lats (com `upgrade`), però elimina els paquets obsolets i instal·la paquets adicionals per satisfer les dependències:

`apt-get dist-upgrade`
