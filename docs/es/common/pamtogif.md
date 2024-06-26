---
layout: page
title: common/pamtogif (español)
description: "Convierte una imagen Netpbm en una imagen GIF no animada."
content_hash: 8d3152c5312a37b6748744aedc57fe11008a15dd
last_modified_at: 2024-05-04
related_topics:
  - title: English version
    url: /en/common/pamtogif.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtogif

Convierte una imagen Netpbm en una imagen GIF no animada.
Vea también: `giftopnm`, `gifsicle`.
Más información: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Convierte una imagen Netpbm en una imagen GIF no animada:

`pamtogif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_de_salida.gif</span>

- Marca el color especificado como transparente en el archivo GIF de salida:

`pamtogif -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_de_salida.gif</span>

- Incluye el texto especificado como comentario en el archivo GIF de salida:

`pamtogif -comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¡Hola Mundo!</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen_de_salida.gif</span>
