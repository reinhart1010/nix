---
layout: page
title: linux/toolbox-init-container (español)
description: "Inicializa un contenedor de `toolbox` que está en funcionamiento."
content_hash: 781f7c41c23454def457867ffc1f220b18df475c
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-init-container.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-init-container.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-init-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox init-container

Inicializa un contenedor de `toolbox` que está en funcionamiento.
Este comando no debe ser ejecutado por el usuario, y no puede ser ejecutado en el host.
Más información: <https://manned.org/toolbox-init-container.1>.

- Inicializa un `toolbox` que está en funcionamiento:

`toolbox init-container --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gid</span>` --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_home</span>` --home-link --media-link --mnt-link --monitor-host --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>` --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>
