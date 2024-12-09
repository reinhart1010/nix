---
layout: page
title: common/podman (español)
description: "Herramienta de gestión sencilla para pods, contenedores e imágenes."
content_hash: f3da3eb7b7ca4483f0649a37f8301554fbf7d486
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/podman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman

Herramienta de gestión sencilla para pods, contenedores e imágenes.
Podman proporciona una línea de comando comparable con Docker-CLI. En pocas palabras: `alias docker=podman`.
Más información: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Lista todos los contenedores (ambos en funcionamiento y detenidos):

`podman ps --all`

- Crea un contenedor desde una imagen con un nombre personalizado:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>

- Inicia o detiene un contenedor existente:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Extrae una imagen de un registro (Docker Hub predeterminado):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>

- Muestra la lista de imágenes ya descargadas:

`podman images`

- Abre una interfaz de comando dentro de un contenedor ya en funcionamiento:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Quita un contenedor detenido:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Muestra los registros de uno o más contenedores y muestra el registro (log):

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_contenedor</span>
