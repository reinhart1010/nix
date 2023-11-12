---
layout: page
title: linux/apt-get (español)
description: "Herramienta de gestión de paquete para distribuciones basadas en Debian."
content_hash: 2969fc6f4221c2621eaf748ee703765963af7ee8
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-get

Herramienta de gestión de paquete para distribuciones basadas en Debian.
Buscar paquetes utilizando `apt-cache`.
Más información: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar este comando antes que cualquier otro comando `apt-get`):

`apt-get update`

- Instala un paquete o actualizarlo a su última versión disponible:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete y sus archivos de configuración:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes instalados a sus nuevas versiones disponibles:

`apt-get upgrade`

- Elimina todos los paquetes innecesarios:

`apt-get autoremove`

- Actualiza paquetes instalados (como `upgrade`), pero elimina paquetes obsoletos e instala paquetes adiciones para satisfacer nuevas dependencias:

`apt-get dist-upgrade`
