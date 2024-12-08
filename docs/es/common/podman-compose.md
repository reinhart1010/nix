---
layout: page
title: common/podman-compose (español)
description: "Ejecuta y gestiona la definición del contenedor según la especificación de composición (Compose Specification)."
content_hash: 77201a5ebd4e60003d1bc07848e61dc1622cfe0a
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman-compose

Ejecuta y gestiona la definición del contenedor según la especificación de composición (Compose Specification).
Más información: <https://github.com/containers/podman-compose>.

- Lista todos los contenedores en funcionamiento:

`podman-compose ps`

- Crea e inicia todos los contenedores en segundo plano utilizando un `docker-compose.yml` local:

`podman-compose up -d`

- Inicia todos los contenedores, construyendo si es necesario:

`podman-compose up --build`

- Inicia todos los contenedores usando un archivo de composición alterno:

`podman-compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.yaml</span>` up`

- Detiene todos los contenedores en funcionamiento:

`podman-compose stop`

- Quita todos los contenedores, redes y volúmenes:

`podman-compose down --volumes`

- Sigue los registros de un contenedor (omite todos los nombres de los contenedores):

`podman-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Ejecuta un comando de una sola vez en un servicio sin puertos mapeados:

`podman-compose run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_servicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
