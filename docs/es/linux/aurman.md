---
layout: page
title: linux/aurman (español)
description: "Una utilidad de Arch Linux para construir e instalar paquetes desde el repositorio de usuarios de Arch (AUR)."
content_hash: bdda1ac6be251d232e7a566e355f2b85023ad82c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aurman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aurman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aurman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aurman

Una utilidad de Arch Linux para construir e instalar paquetes desde el repositorio de usuarios de Arch (AUR).
Vea también: `pacman`.
Más información: <https://github.com/polygamma/aurman>.

- Sincroniza y actualiza todos los paquetes:

`aurman --sync --refresh --sysupgrade`

- Sincroniza y actualiza todos los paquetes sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman --sync --refresh --sysupgrade --noedit`

- Instala un nuevo paquete:

`aurman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un nuevo paquete sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman --sync --noedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un nuevo paquete sin pedir confirmación:

`aurman --sync --noedit --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca en la base de datos de paquetes una palabra clave en los repositorios oficiales y AUR:

`aurman --sync --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>

- Elimina un paquete y sus dependencias:

`aurman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Limpia la caché de paquetes (usa dos banderas `--clean` para limpiar todos los paquetes):

`aurman --sync --clean`
