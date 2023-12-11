---
layout: page
title: linux/grub-mkconfig (español)
description: "Genera un archivo de configuracion de GRUB."
content_hash: 796c2c2899ae8ecea1a7f440bf5e1ce7f1d237a4
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/linux/grub-mkconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-mkconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-mkconfig

Genera un archivo de configuracion de GRUB.
Más información: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkconfig.html>.

- Ejecuta el comando solo e imprime la salida a `stdout`:

`sudo grub-mkconfig`

- Genera el archivo de configuración:

`sudo grub-mkconfig --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/boot/grub/grub.cfg</span>

- Imprime la página de ayuda:

`grub-mkconfig --help`
