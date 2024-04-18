---
layout: page
title: linux/dnf5 (español)
description: "Programa de gestión de paquetes para RHEL, Fedora y CentOS (reemplaza a dnf, que a su vez reemplazó a yum)."
content_hash: fb01a632e999461b3410f0fbefc5a857f087d478
last_modified_at: 2024-04-18
related_topics:
  - title: English version
    url: /en/linux/dnf5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf5

Programa de gestión de paquetes para RHEL, Fedora y CentOS (reemplaza a dnf, que a su vez reemplazó a yum).
DNF5 es una reescritura en C++ del gestor de paquetes DNF con mejor rendimiento y menor tamaño.
Para comandos equivalentes en otros gestores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Más información: <https://dnf5.readthedocs.io/>.

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`sudo dnf5 upgrade`

- Busca paquetes mediante palabras clave:

`dnf5 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave1 palabra_clave2 ...</span>

- Muestra detalles sobre un paquete:

`dnf5 info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala nuevos paquetes (Nota: usa la opción `-y` para saltar todas las confirmaciones):

`sudo dnf5 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Elimina paquetes:

`sudo dnf5 remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Lista paquetes instalados:

`dnf5 list --installed`

- Busca que paquetes proporcionan un comando determinado:

`dnf5 provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Elimina o expira los datos almacenados en caché:

`sudo dnf5 clean all`
