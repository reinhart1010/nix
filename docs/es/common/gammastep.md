---
layout: page
title: common/gammastep (español)
description: "Ajusta la temperatura del color de la pantalla según la hora del día."
content_hash: 433d03fdfe31ccb35472b0ffedab4287afdb7b38
last_modified_at: 2024-02-11
related_topics:
  - title: English version
    url: /en/common/gammastep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Gammastep

Ajusta la temperatura del color de la pantalla según la hora del día.
Más información: <https://gitlab.com/chinstrap/gammastep>.

- Activa Gammastep con una [t]emperatura específica durante el día (por ejemplo, 5700k) y por la noche (por ejemplo, 3600k):

`gammastep -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5700</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Activa Gammastep con una [l]ocación personalizada especificada manualmente:

`gammastep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latitud</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitud</span>

- Activa Gammastep con un [b]rillo de pantalla específico durante el día (por ejemplo, 70%) y la noche (por ejemplo, 40%), con un brillo mínimo del 10% y uno máximo del 100%:

`gammastep -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.4</span>

- Activa Gammastep con niveles de [g]ama personalizados (entre 0 y 1):

`gammastep -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rojo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verde</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">azul</span>

- Activa Gammastep con una temperatura de color c[O]nstante e invariable:

`gammastep -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temperatura</span>

- Restablece los ajustes de temperatura aplicados por Gammastep:

`gammastep -x`
