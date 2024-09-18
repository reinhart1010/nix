---
layout: page
title: linux/a2query (español)
description: "Recupera la configuración en tiempo de ejecución de Apache en sistemas operativos basados en Debian."
content_hash: 171a59d555ba446bb1fb68a0512c7476b2eab724
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
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
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

Recupera la configuración en tiempo de ejecución de Apache en sistemas operativos basados en Debian.
Más información: <https://manned.org/a2query>.

- Lista módulos de Apache habilitados:

`sudo a2query -m`

- Comprueba si un módulo específico está instalado:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Lista hosts virtuales habilitados:

`sudo a2query -s`

- Muestra el Módulo de Procesamiento Múltiple actualmente habilitado:

`sudo a2query -M`

- Muestra la versión de Apache:

`sudo a2query -v`
