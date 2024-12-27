---
layout: page
title: linux/toolbox-rm (español)
description: "Elimina uno o más contenedores de `toolbox`."
content_hash: 06a0a704b95e8e6a72c01c5261452cffc0b204f8
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox rm

Elimina uno o más contenedores de `toolbox`.
Vea también: `toolbox rmi`.
Más información: <https://manned.org/toolbox-rm.1>.

- Quita un contenedor de `toolbox`:

`toolbox rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Quita todos los contenedores de `toolbox`:

`toolbox rm --all`

- Fuerza la eliminación de un contenedor de `toolbox` activo actualmente:

`toolbox rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>
