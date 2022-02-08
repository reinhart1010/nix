---
layout: page
title: common/docker-compose (español)
description: "Ejecuta y gestiona múltiples contenedores Docker."
content_hash: 951cf5b480206d5646fec16c039696b0e8202fb6
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

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-compose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker-compose

Ejecuta y gestiona múltiples contenedores Docker.
Más información: <https://docs.docker.com/compose/reference/>.

- Lista los contenedores en ejecución:

`docker-compose ps`

- Crea e inicia todos los contenedores en segundo plano usando el archivo `docker-compose.yml` en el directorio actual:

`docker-compose up -d`

- Inicia todos los contenedores y reconstruye si es ncesario:

`docker-compose up --build`

- Inicia todos los contenedores usando un archivo compose alternativo:

`docker-compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` up`

- Detiene todos los contenedores en ejecución:

`docker-compose stop`

- Detiene y elimina todos los contenedores, redes, imágenes y volúmenes:

`docker-compose down --rmi all --volumes`

- Sigue los registros de todos los contenedores:

`docker-compose logs --follow`

- Sigue los registros de un contenedor específico:

`docker-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_contenedor</span>
