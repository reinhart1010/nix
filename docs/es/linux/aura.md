---
layout: page
title: linux/aura (español)
description: "El gestor de paquetes Aura: un gestor de paquetes seguro y multilingüe para Arch Linux y el AUR."
content_hash: 5aaac31ec0682071c5fdd3b2bd5be53ebc16756d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aura.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aura.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aura.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aura

El gestor de paquetes Aura: un gestor de paquetes seguro y multilingüe para Arch Linux y el AUR.
Más información: <https://github.com/fosskers/aura>.

- Busca paquetes en los repositorios oficiales y AUR:

`aura --aursync --both --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave|expresión_regular</span>

- Instala un paquete desde el AUR:

`aura --aursync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes del AUR en modo detallado y elimina todas las dependencias de construcción:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Instala un paquete desde los repositorios oficiales:

`aura --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Sincroniza y actualiza todos los paquetes desde los repositorios oficiales:

`aura --sync --refresh --sysupgrade`

- Reemplaza un paquete con uno más antiguo usando la caché de paquetes:

`aura --downgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete y sus dependencias:

`aura --remove --recursive --unneeded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina paquetes huérfanos (instalados como dependencias pero no requeridos por ningún paquete):

`aura --orphans --abandon`
