---
layout: page
title: linux/dos2unix (español)
description: "Cambia saltos de línea con formato DOS a saltos de línea con formato Unix."
content_hash: eefc9c993868b3fcf7ce923d5d622e6f7309c60d
last_modified_at: 2024-10-29
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/dos2unix.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dos2unix

Cambia saltos de línea con formato DOS a saltos de línea con formato Unix.
Reemplaza CRLF con LF.
Vea también `unix2dos`, `unix2mac`, y `mac2unix`.
Más información: <https://manned.org/dos2unix>.

- Cambia los saltos de línea de un archivo:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea una copia con saltos de línea en formato Unix:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/nuevo</span>

- Muestra información de un archivo:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Mantiene/añade/elimina Marca de Orden de Byte (Byte Order Mark):

`dos2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
