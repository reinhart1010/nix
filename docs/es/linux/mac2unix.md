---
layout: page
title: linux/mac2unix (español)
description: "Cambia los finales de línea de estilo macOS al estilo Unix."
content_hash: 018d3b37935327a9a28cac09280a04bf1bb11194
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/mac2unix.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mac2unix.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mac2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mac2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mac2unix

Cambia los finales de línea de estilo macOS al estilo Unix.
Reemplaza CR con LF.
Vea también `unix2dos`, `unix2mac` y `dos2unix`.
Más información: <https://manned.org/mac2unix>.

- Cambia los finales de línea de un archivo:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea una copia con finales de línea de estilo Unix:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nuevo_archivo</span>

- Muestra información del archivo:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Mantiene/añade/elimina marca de orden de byte (Byte Order Mark):

`mac2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
