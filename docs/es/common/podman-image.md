---
layout: page
title: common/podman-image (español)
description: "Gestiona imágenes Docker."
content_hash: ac6d5fa22e624a75408a2c94585b83496a2862db
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-image.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman image

Gestiona imágenes Docker.
Vea también: `podman build`, `podman import` y `podman pull`.
Más información: <https://docs.podman.io/en/latest/markdown/podman-image.1.html>.

- Lista imágenes locales de Docker:

`podman image ls`

- Elimina imágenes locales de Docker no utilizadas:

`podman image prune`

- Elimina todas las imágenes no utilizadas (no sólo aquellas sin una etiqueta):

`podman image prune --all`

- Muestra la historia de una imagen Docker local:

`podman image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>
