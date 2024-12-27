---
layout: page
title: linux/toolbox-create (español)
description: "Crea un nuevo contenedor de `toolbox`."
content_hash: 9b85309d795e8b1baa2a01af72f61655e453bed3
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/toolbox-create.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/toolbox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox create

Crea un nuevo contenedor de `toolbox`.
Más información: <https://manned.org/toolbox-create.1>.

- Crea un contenedor para una distribución específica:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribución</span>

- Crea un contenedor de `toolbox` para una liberación específica de la distribución actual:

`toolbox create --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">liberación</span>

- Crea un contenedor de `toolbox` con una imagen personalizada:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea un contenedor de `toolbox` de una imagen personalizada de Fedora:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:39</span>

- Crea un contenedor `toolbox` utilizando la imagen predeterminada de Fedora 39:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
