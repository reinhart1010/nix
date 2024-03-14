---
layout: page
title: common/docker-compose (español)
description: "Ejecuta y gestiona aplicaciones Docker multicontenedor."
content_hash: bca2c4b1c71f8b4ad160415cd100d9d70ccf204b
last_modified_at: 2024-03-14
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
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Ejecuta y gestiona aplicaciones Docker multicontenedor.
Más información: <https://docs.docker.com/compose/reference/>.

- Lista todos los contenedores en ejecución:

`docker compose ps`

- Crea e inicia todos los contenedores en segundo plano usando un archivo `docker-compose.yml` desde el directorio actual:

`docker compose up --detach`

- Inicia todos los contenedores, y se reconstruye si es necesario:

`docker compose up --build`

- Inicia todos los contenedores especificando un nombre de proyecto y utilizando un archivo de composición alternativo:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_proyecto</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` up`

- Detiene todos los contenedores en ejecución:

`docker compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker compose logs --follow`

- Sigue los registros de un contenedor específico:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>
