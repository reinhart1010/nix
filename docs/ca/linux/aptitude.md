---
layout: page
title: linux/aptitude (català)
description: "Eina de gestió de paquets per a Debian i Ubuntu."
content_hash: edc7ea627dd572eae37f3e7ae0252be21e147d1e
last_modified_at: 2024-09-18
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
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Eina de gestió de paquets per a Debian i Ubuntu.
Més informació: <https://manned.org/aptitude.8>.

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
