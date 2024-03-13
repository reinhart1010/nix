---
layout: page
title: linux/iwlist (español)
description: "Obtén información detallada de una interfaz inalámbrica."
content_hash: a53cf42a6ec09c849d599f41367030be615bb757
last_modified_at: 2024-03-13
related_topics:
  - title: English version
    url: /en/linux/iwlist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iwlist

Obtén información detallada de una interfaz inalámbrica.
Más información: <https://manned.org/iwlist.8>.

- Muestra la lista de puntos de acceso y células ad-hoc en alcance:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` scan`

- Muestra las frecuencias disponibles en el dispositivo:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` frequency`

- Lista las tasas de bits soportadas por el dispositivo:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` rate`

- Enumera los parámetros de autenticación WPA configurados actualmente:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` auth`

- Enumera todas las claves de cifrado WPA configuradas en el dispositivo:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` wpakeys`

- Enumera los tamaños de clave de cifrado admitidos y todas las claves de cifrado configuradas en el dispositivo:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` keys`

- Enumera los distintos atributos y modos de gestión de energía del dispositivo:

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` power`

- Enumera los elementos de información genéricos configurados en el dispositivo (utilizados para la compatibilidad con WPA):

`iwlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz_inalámbrica</span>` genie`
