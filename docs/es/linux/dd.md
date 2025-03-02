---
layout: page
title: linux/dd (español)
description: "Convierte y copia un archivo."
content_hash: 186b856d2676535a9f7e594430cd0edf77af1663
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Convierte y copia un archivo.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- Crea una unidad USB de arranque a partir de un archivo isohybrid (como `archlinux-xxx.iso`) y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidad_usb</span>` status=progress`

- Clona una unidad a otra con un tamaño de bloque de 4 MiB y descarga las escrituras antes de que el comando termine:

`dd bs=4M conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidad_de_origen</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidad_de_descarga</span>

- Genera un archivo con un número específico de bytes aleatorios utilizando el controlador aleatorio del kernel:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_aleatorio</span>

- Compara el rendimiento de escritura de un disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/fichero_1GB</span>

- Crea una copia de seguridad del sistema en un archivo IMG (puede restaurarla más tarde intercambiando `if` y `of`), y muestra el progreso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidad_dispositivo</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.img</span>` status=progress`

- Comprueba el progreso de una operación `dd` en curso (ejecute este comando desde otro intérprete de comandos):

`kill -USR1 $(pgrep -x dd)`
