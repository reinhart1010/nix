---
layout: page
title: common/docker-compose (español)
description: "Ejecuta y gestiona múltiples contenedores Docker."
content_hash: a2daa70a0b87e34d9752f6265f78ea7c61f2c2fe
last_modified_at: 2023-02-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---
# docker compose

Ejecuta y gestiona múltiples contenedores Docker.
Más información: <https://docs.docker.com/compose/reference/>.

- Lista los contenedores en ejecución:

`docker compose ps`

- Crea e inicia todos los contenedores en segundo plano usando el archivo `docker-compose.yml` en el directorio actual:

`docker compose up --detach`

- Inicia todos los contenedores y reconstruye si es ncesario:

`docker compose up --build`

- Inicia todos los contenedores usando un archivo compose alternativo:

`docker compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` up`

- Detiene todos los contenedores en ejecución:

`docker compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker compose logs --follow`

- Sigue los registros de un contenedor específico:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_contenedor</span>
