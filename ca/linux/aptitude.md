---
layout: page
title: linux/aptitude (català)
description: "Eina de gestió de paquets per a Debian i Ubuntu."
content_hash: 6cf4129cac227cba6138052369f2d6f5a4b9b12c
related_topics:
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---
# aptitude

Eina de gestió de paquets per a Debian i Ubuntu.
Més informació: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Sincronitza la llista de paquets i versions disponibles (es recomana executar aquest commandament abans que qualsevol altre `aptitude`):

`aptitude update`

- Instal·lar un nou paquet i les seves dependències:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Buscar un paquet:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Cercar un paquet instal·lat (`?installed` es un terme de cerca de `aptitude`):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>`)'`

- Elimina un paquet i tots els paquets que depenen d'ell:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Actualitza tots els paquets a les noves versions disponibles:

`aptitude upgrade`

- Actualitza paquets instal·lats (com `aptitude upgrade`), però elimina els paquets obsolets i instal·la paquets nous per satisfer les dependències:

`aptitude full-upgrade`

- Manté un paquet perquè no sigui actualitzat automàticament:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`)'`
