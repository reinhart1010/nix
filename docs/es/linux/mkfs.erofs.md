---
layout: page
title: linux/mkfs.erofs (español)
description: "Crea un sistema de archivos EROFS en una imagen."
content_hash: 488d724c39d8c38de6cf8af05d930f77ad6a0699
last_modified_at: 2024-08-07
related_topics:
  - title: English version
    url: /en/linux/mkfs.erofs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.erofs

Crea un sistema de archivos EROFS en una imagen.
Más información: <https://erofs.docs.kernel.org/en/latest/>.

- Crea un sistema de archivos EROFS basado en el directorio raíz:

`mkfs.erofs image.erofs root/`

- Crea una imagen EROFS con un UUID específico:

`mkfs.erofs -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID</span>` image.erofs root/`

- Crea una imagen EROFS comprimida:

`mkfs.erofs -zlz4hc image.erofs root/`

- Crea una imagen EROFS en la que todos los archivos pertenezcan a root:

`mkfs.erofs --all-root image.erofs root/`
