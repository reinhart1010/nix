---
layout: page
title: linux/toolbox-rmi (español)
description: "Elimina imágenes de `toolbox`."
content_hash: aa8381866a574179ddcd6778760354b6898e4b8f
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-rmi.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-rmi.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox rmi

Elimina imágenes de `toolbox`.
Vea también: `toolbox rm`.
Más información: <https://manned.org/toolbox-rmi.1>.

- Quita una o más imágenes de `toolbox`:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_imagen1 nombre_de_la_imagen2 ...</span>

- Quita todas las imágenes de `toolbox`:

`toolbox rmi --all`

- Fuerza la eliminación de una imagen de `toolbox` que está siendo utilizado actualmente por un contenedor (el contenedor será eliminado también):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_imagen</span>
