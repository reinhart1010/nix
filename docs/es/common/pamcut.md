---
layout: page
title: common/pamcut (español)
description: "Corta una región rectangular de una imagen Netpbm."
content_hash: c76006e147d9b31ddb864c5642a509b21823ebb9
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/pamcut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pamcut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamcut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamcut

Corta una región rectangular de una imagen Netpbm.
Vea también: `pamcrop`, `pamdice`, `pamcomp`.
Más información: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Descarta la cantidad de columnas/filas especificadas a cada lado de la imagen:

`pamcut -cropleft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -cropright `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -croptop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -cropbottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>

- Mantiene solo las columnas entre las columnas especificadas (inclusivamente):

`pamcut -left `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -right `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>

- Llena áreas perdidas con píxeles negros si el rectángulo especificado no se encuentra completamente dentro de la imagen de entrada:

`pamcut -top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -bottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` -pad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/imagen.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>
