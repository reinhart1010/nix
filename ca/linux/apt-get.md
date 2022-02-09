---
layout: page
title: linux/apt-get (català)
description: "Eina de gestió de paquets per a distribucions basades en Debian."
content_hash: 9eaadaf76eb44ac9dd9c184f91a7d92716527904
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Eina de gestió de paquets per a distribucions basades en Debian.
Busca paquets utilizant `apt-cache`.
Més información: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

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
