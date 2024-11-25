---
layout: page
title: common/pnmcolormap (español)
description: "Crea mapa de colores cuantizado para una imagen PNM."
content_hash: 00abc9f77bedfbe06fe989d9c410a100bacf9b77
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/pnmcolormap.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pnmcolormap.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pnmcolormap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmcolormap

Crea mapa de colores cuantizado para una imagen PNM.
Más información: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Genera una imagen usando sólo 'n_colores' o menos colores lo más cerca posible de la imagen de entrada:

`pnmcolormap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colores</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>

- Utiliza la estrategia de splitspread para determinar los colores de salida, posiblemente produciendo un mejor resultado para imágenes con detalles pequeños:

`pnmcolormap -splitspread `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colores</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>

- Ordena el mapa de colores resultante, que es útil para comparar los mapas de colores:

`pnmcolormap -sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.ppm</span>
