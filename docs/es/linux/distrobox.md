---
layout: page
title: linux/distrobox (español)
description: "Utiliza cualquier distribución Linux dentro de su terminal en un contenedor."
content_hash: f14982a72041f3621ec0ae530b1b4a2ad4068f64
last_modified_at: 2024-12-31
related_topics:
  - title: English version
    url: /en/linux/distrobox.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/distrobox.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/distrobox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># distrobox

Utiliza cualquier distribución Linux dentro de su terminal en un contenedor.
Instala y utiliza paquetes dentro de la misma, mientras se integra estrechamente con el sistema operativo anfitrión, compartiendo el almacenamiento (directorio `home`) y el hardware.
Nota: Utiliza Podman o Docker para crear sus contenedores.
Más información: <https://github.com/89luca89/distrobox>.

- Muestra documentación para crear contenedores:

`tldr distrobox-create`

- Muestra documentación para listar la información del contenedor:

`tldr distrobox-list`

- Muestra documentación para entrar en el contenedor:

`tldr distrobox-enter`

- Muestra documentación para ejecutar un comando en el anfitrión desde dentro de un contenedor:

`tldr distrobox-host-exec`

- Muestra documentación para exportar aplicación/servicio/binario del contenedor al host:

`tldr distrobox-export`

- Muestra documentación para actualizar contenedores:

`tldr distrobox-upgrade`

- Muestra documentación para detener los contenedores:

`tldr distrobox-stop`

- Muestra documentación para la eliminación de contenedores:

`tldr distrobox-rm`
