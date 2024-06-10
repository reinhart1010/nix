---
layout: page
title: osx/dd (español)
description: "Convierte y copia un archivo."
content_hash: 77fd6db3dc0cf2262ba279f8fb087c56d7c8e790
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Convierte y copia un archivo.
Más información: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Crea una unidad USB de arranque desde un archivo isohybrid (como `archlinux-xxx.iso`) y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_usb</span>` status=progress`

- Clona una unidad a otra unidad con un bloque de 4 MB, ignora el error y muestra el progreso:

`dd bs=4m conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de origen</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de destino</span>` status=progress`

- Genera un archivo con un número específico de bytes aleatorios utilizando el controlador aleatorio del núcleo:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_aleatorio</span>

- Compara el rendimiento de escritura de un disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/para/archivo_1GB</span>

- Genera una copia de seguridad del sistema en un archivo IMG y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_unidad</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.img</span>` status=progress`

- Comprueba el progreso de una operación `dd` en curso (ejecuta este comando desde otro intérprete de comandos):

`kill -USR1 $(pgrep ^dd)`
