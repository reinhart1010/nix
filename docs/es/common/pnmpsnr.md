---
layout: page
title: common/pnmpsnr (español)
description: "Calcula la diferencia entre dos imágenes."
content_hash: a05916207330fe3631db758e205c075e494e8bef
last_modified_at: 2024-02-06
related_topics:
  - title: English version
    url: /en/common/pnmpsnr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmpsnr

Calcula la diferencia entre dos imágenes.
Más información: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- Calcula la diferencia, es decir, la relación señal-ruido (PSNR) entre dos imágenes:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>

- Compara los componentes de color en lugar de los componentes de luminancia y crominancia de las imágenes:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>` -rgb`

- Ejecuta en modo de comparación, es decir, solo la salida `nomatch` o `match` dependiendo de si el cálculo PSNR supera `n` o no:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>` -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Ejecuta en modo comparación y compara los componentes individuales de la imagen, es decir, Y, Cb y Cr, con los umbrales correspondientes:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>` -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_Y</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_Cb</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_Cr</span>

- Ejecuta en modo comparación y compara los componentes individuales de la imagen, es decir, rojo, verde y azul con los umbrales correspondientes:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>` -rgb -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_rojo</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_verde</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umbral_azul</span>

- Produce salida legible para máquinas:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.pnm</span>` -machine`
