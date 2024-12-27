---
layout: page
title: linux/toolbox-enter (español)
description: "Ingresa a un contenedor `toolbox` para usarlo interactivamente."
content_hash: f1b0e38df1355a35b84e61ae9d017676796e59ba
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-enter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox enter

Ingresa a un contenedor `toolbox` para usarlo interactivamente.
Vea también: `toolbox run`.
Más información: <https://manned.org/toolbox-enter.1>.

- Entra a un contenedor de `toolbox` utilizando la imagen predeterminada de una distribución específica:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribución</span>

- Entra a un contenedor de `toolbox` utilizando la imagen predeterminada de una liberación específica de la distribución actual:

`toolbox enter --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">liberación</span>

- Entra a un contenedor de `toolbox` utilizando la imagen predeterminada de Fedora 39:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
