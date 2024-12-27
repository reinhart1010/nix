---
layout: page
title: linux/distrobox-create (español)
description: "Crea un contenedor Distrobox. Véase también: `tldr distrobox`."
content_hash: 43759b05622fbd91cd675855009c87d98bed04af
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/distrobox-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-create

Crea un contenedor Distrobox. Véase también: `tldr distrobox`.
El contenedor creado se integrará estrechamente con el anfitrión, permitiendo compartir el directorio HOME del usuario, almacenamiento externo, dispositivos USB externos, aplicaciones gráficas (X11/Wayland) y audio.
Más información: <https://distrobox.it/usage/distrobox-create>.

- Crea un contenedor Distrobox utilizando la imagen Ubuntu:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Clona un contenedor Distrobox:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor_clonado</span>
