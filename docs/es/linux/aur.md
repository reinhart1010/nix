---
layout: page
title: linux/aur (español)
description: "Construye paquetes desde el AUR y gestiona repositorios locales."
content_hash: 20686a42fa049e7cc8e8b1bb3dd9117ffd54fbe7
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/linux/aur.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aur

Construye paquetes desde el AUR y gestiona repositorios locales.
Nota: Es necesario establecer un repositorio local en `/etc/pacman.conf` e instalar `vifm` para que funcione completamente.
Más información: <https://github.com/aurutils/aurutils>.

- Busca un paquete en la base de datos del AUR:

`aur search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Descarga un paquete y sus dependencias desde el AUR, los compila y añade a un repositorio local:

`aur sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- [l]ista paquetes disponibles en tu repositorio local:

`aur repo --list`

- Act[u]aliza los paquetes del repositorio local:

`aur sync --upgrades`

- Instala un paquete sin ver los cambios en Vim y sin confirmar la instalación de dependencias:

`aur sync --noview --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
