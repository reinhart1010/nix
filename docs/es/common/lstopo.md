---
layout: page
title: common/lstopo (español)
description: "Muestra la topología de hardware del sistema."
content_hash: 0c6d01b423754bece2f0d3cfd5b055fad5836c47
last_modified_at: 2024-05-19
related_topics:
  - title: English version
    url: /en/common/lstopo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lstopo

Muestra la topología de hardware del sistema.
Más información: <https://manned.org/lstopo>.

- Muestra la topología resumida del sistema en una ventana gráfica (o imprime en consola si no se dispone de una sesión gráfica):

`lstopo`

- Muestra la topología completa del sistema sin resúmenes:

`lstopo --no-factorize`

- Muestra la topología resumida del sistema sólo con índices físicos (es decir, tal y como la ve el sistema operativo):

`lstopo --physical`

- Escribe la topología completa del sistema en un archivo con el formato especificado:

`lstopo --no-factorize --output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console|ascii|tex|fig|svg|pdf|ps|png|xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra datos en monocromo o escala de grises:

`lstopo --palette `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|grey</span>
