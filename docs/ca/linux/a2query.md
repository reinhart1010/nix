---
layout: page
title: linux/a2query (català)
description: "Recupera la configuració del temps d'execució d'Apache en sistemes operatius basats en Debian."
content_hash: 9ee6559386d4b436aa0cc90beb0ba1c1284833f7
related_topics:
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Recupera la configuració del temps d'execució d'Apache en sistemes operatius basats en Debian.
Més informació: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Llista mòduls Apache activats:

`sudo a2query -m`

- Comprova si un mòdul específic està instal·lat:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_mòdul</span>

- Llista els hosts virtuals activats:

`sudo a2query -s`

- Mostra el mòdul de processament múltiple:

`sudo a2query -M`

- Mostra la versió d'Apache:

`sudo a2query -v`
