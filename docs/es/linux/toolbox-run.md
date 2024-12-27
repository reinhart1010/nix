---
layout: page
title: linux/toolbox-run (español)
description: "Ejecuta un comando en un contenedor existente de `toolbox`."
content_hash: 9e62f05f31fc3c3df91dd765c1bb771c41b92589
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-run.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-run.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox run

Ejecuta un comando en un contenedor existente de `toolbox`.
Vea también: `toolbox enter`.
Más información: <https://manned.org/toolbox-run>.

- Ejecuta un comando dentro de un contenedor específico `toolbox`:

`toolbox run --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta un comando dentro de un contenedor `toolbox` para una liberación específica de una distribución:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribución</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lanzamiento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta `emacs` dentro de un contenedor `toolbox` utilizando la imagen predeterminada de Fedora 39:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>
