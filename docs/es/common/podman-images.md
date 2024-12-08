---
layout: page
title: common/podman-images (español)
description: "Gestiona imágenes de Podman."
content_hash: 26f834c1e305f5396767a48b84ef3de164339a6b
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-images.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-images.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-images.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman images

Gestiona imágenes de Podman.
Más información: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- Lista todas las imágenes de Podman:

`podman images`

- Lista todas las imágenes Podman incluyendo intermedias:

`podman images --all`

- Lista en modo silencioso (sólo ID numérico):

`podman images --quiet`

- Lista todas las imágenes Podman no utilizadas por ningún contenedor:

`podman images --filter dangling=true`

- Lista las imágenes que contienen una subcadena en su nombre:

`podman images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*imagen|imagen*</span>`"`
