---
layout: page
title: linux/unix2dos (español)
description: "Cambia los finales de línea de estilo Unix al estilo DOS."
content_hash: 9e456bcee81179e3aecdd7861992a213d40ee5c5
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/unix2dos.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/unix2dos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/unix2dos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2dos

Cambia los finales de línea de estilo Unix al estilo DOS.
Reemplaza LF con CRLF.
Vea también `unix2mac`, `dos2unix` y `mac2unix`.
Más información: <https://manned.org/unix2dos>.

- Cambia los finales de línea de un archivo:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea una copia con finales de línea de estilo DOS:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_nuevo</span>

- Muestra información del archivo:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Mantiene/añade/elimina marca de bit de orden (Byte Order Mark):

`unix2dos --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
