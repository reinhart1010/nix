---
layout: page
title: linux/grub-mkconfig (español)
description: "Generar un archivo de configuracion de GRUB."
content_hash: b8e16ce90a294e9b5af6112795e63a1e42dcd710
last_modified_at: 2023-09-26
related_topics:
  - title: English version
    url: /en/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-mkconfig.html
    icon: bi bi-globe
---
# grub-mkconfig

Generar un archivo de configuracion de GRUB.
Más información: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- Ejecutar el comando solo e imprimir la salida a `stdout`:

`sudo grub-mkconfig`

- Generar el archivo de configuracion:

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- Imprimir la pagina de ayuda:

`grub-mkconfig --help`
