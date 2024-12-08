---
layout: page
title: common/podman-build (español)
description: "Herramienta que no corre como servicio (daemon) para construir imágenes de contenedores."
content_hash: 42e5c981d9497ae00be30a5169ddfe0d196ae652
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman build

Herramienta que no corre como servicio (daemon) para construir imágenes de contenedores.
Podman proporciona una línea de comando comparable con Docker-CLI. En pocas palabras: `alias docker=podman`.
Más información: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Crea una imagen usando un `Dockerfile` o `Containerfile` en el directorio especificado:

`podman build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea una imagen con una etiqueta especificada:

`podman build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_imagen:version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea una imagen de un archivo no estándar:

`podman build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Archivo_contenedor.different</span>` .`

- Crea una imagen sin usar ninguna imagen previamente almacenada en caché:

`podman build --no-cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea una imagen suprimiendo cualquier mensaje informativo (output):

`podman build --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
