---
layout: page
title: osx/dd (español)
description: "Convierte y copia un archivo."
content_hash: 63d72fe8a7eeadcab67a52ed0540073697536f2e
last_modified_at: 2023-08-22
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dd

Convierte y copia un archivo.
Más información: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Crea una unidad USB de arranque desde un archivo isohybrid (como `archlinux-xxx.iso`) y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_usb</span>` status=progress`

- Clona una unidad a otra unidad con un bloque de 4 MB, ignora el error y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de origen</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de destino</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` conv=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noerror</span>` status=progress`

- Genera un fichero de 100 bytes aleatorios utilizando el controlador aleatorio del kernel:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_aleatorio</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Compara el rendimiento de escritura de un disco:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/para/archivo_1GB</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>

- Genera una copia de seguridad del sistema en un archivo IMG y muestra el progreso:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo_unidad</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.img</span>` status=progress`

- Restaura una unidad desde un archivo IMG y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.img</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidad_dispositivo</span>` status=progress`

- Comprueba el progreso de una operación dd en curso (ejecuta este comando desde otro shell):

`kill -USR1 $(pgrep ^dd)`
