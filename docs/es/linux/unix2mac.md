---
layout: page
title: linux/unix2mac (español)
description: "Cambia los finales de línea de estilo Unix al estilo macOS."
content_hash: 782294e5fc80e4817df1f1a8a89189202da35d1c
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/unix2mac.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2mac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/unix2mac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2mac

Cambia los finales de línea de estilo Unix al estilo macOS.
Reemplaza LF con CR.
Vea también `unix2dos`, `dos2unix` y `mac2unix`.
Más información: <https://manned.org/unix2mac>.

- Cambia los finales de línea de un archivo:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea una copia con finales de línea de estilo macOS:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_nuevo</span>

- Muestra información del archivo:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Mantiene/añade/elimina marca de orden de byte (Byte Order Mark):

`unix2mac --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
