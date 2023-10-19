---
layout: page
title: linux/aptitude (español)
description: "Herramienta de gestión de paquetes para Debian y Ubuntu."
content_hash: eee9a1b55ba613c99e76baf6f4b9b1849fb6403f
last_modified_at: 2023-10-19
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
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
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---
# aptitude

Herramienta de gestión de paquetes para Debian y Ubuntu.
Más información: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Sincroniza la lista de paquetes y versiones disponible (se recomienda ejecutar este comando antes que cualquier otro comando `aptitude`):

`aptitude update`

- Instalar un nuevo paquete y sus dependencias:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Buscar un paquete:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Buscar un paquete instalado (`?installed` es un término de búsqueda de `aptitude`):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`)'`

- Elimina un paquete y todos los paquetes que dependen de él:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes a sus nuevas versiones disponibles:

`aptitude upgrade`

- Actualiza paquetes instalados (como `aptitude upgrade`), elimina los paquetes obsoletos e instala paquetes adicionales para satisfacer sus dependencias:

`aptitude full-upgrade`

- Mantiene un paquete instalado para que no sea actualizado automáticamente:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`)'`
