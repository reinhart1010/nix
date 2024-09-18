---
layout: page
title: linux/apt-get (español)
description: "Utilidad de gestión de paquetes para Debian y Ubuntu."
content_hash: 8551f1d5809e3dabeec42dfb6cebf05995a81657
last_modified_at: 2024-09-18
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
  - title: Indonesia version
    url: /id/linux/apt-get.html
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

Utilidad de gestión de paquetes para Debian y Ubuntu.
Búsqueda de paquetes mediante `apt-cache`.
Más información: <https://manned.org/apt-get.8>.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar esto antes de otros comandos `apt-get`):

`apt-get update`

- Instala un paquete o lo actualiza a la última versión disponible:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete y sus archivos de configuración:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes instalados a sus versiones más recientes:

`apt-get upgrade`

- Limpia el repositorio local: elimina los archivos de paquetes (`.deb`) de descargas interrumpidas que ya no pueden descargarse:

`apt-get autoclean`

- Elimina todos los paquetes que ya no sean necesarios:

`apt-get autoremove`

- Actualiza los paquetes instalados (como `upgrade`), pero eliminando los paquetes obsoletos e instalando paquetes adicionales para satisfacer las nuevas dependencias:

`apt-get dist-upgrade`
