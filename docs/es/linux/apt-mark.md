---
layout: page
title: linux/apt-mark (español)
description: "Herramienta para cambiar el estado de los paquetes instalados."
content_hash: 1271d64c5ce324ce25c3776cb62ff9fb09c303f3
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Herramienta para cambiar el estado de los paquetes instalados.
Más información: <https://manned.org/apt-mark.8>.

- Marca un paquete como instalado automáticamente:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Mantiene un paquete en su versión actual y evita que se actualice:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Permite que un paquete pueda ser actualizado de nuevo:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Muestra los paquetes instalados manualmente:

`apt-mark showmanual`

- Muestra los paquetes mantenidos que no son actualizados:

`apt-mark showhold`
