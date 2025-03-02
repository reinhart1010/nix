---
layout: page
title: linux/lxc-create (español)
description: "Crea contenedores linux."
content_hash: 3d4088c10e25e5a776c6a59a92ce0fdccd6d9641
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/lxc-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lxc-create

Crea contenedores linux.
Más información: <https://linuxcontainers.org/lxc/getting-started>.

- Crea un contenedor interactivamente en `/var/lib/lxc/`:

`lxc-create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor</span>` --template download`

- Crea un contenedor en un directorio de destino:

`lxc-create --lxcpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/directorio/</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contenedor</span>` --template download`

- Crea un contenedor pasando opciones a una plantilla:

`lxc-create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --template download -- --dist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-distro</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión-de-lanzamiento</span>` --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>
