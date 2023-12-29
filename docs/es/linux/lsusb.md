---
layout: page
title: linux/lsusb (español)
description: "Muestra información sobre los buses USB y los dispositivos conectados a ellos."
content_hash: ed6e675c9ce54af55d0f439e0bb2c84cc9d5181e
last_modified_at: 2023-12-29
related_topics:
  - title: català version
    url: /ca/linux/lsusb.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsusb.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsusb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/lsusb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsusb

Muestra información sobre los buses USB y los dispositivos conectados a ellos.
Más información: <https://manned.org/lsusb>.

- Muestra todos los dispositivos USB disponibles:

`lsusb`

- Lista la jerarquía USB como un árbol:

`lsusb -t`

- Muestra información detallada sobre los dispositivos USB:

`lsusb --verbose`

- Muestra información detallada sobre un dispositivo USB:

`lsusb --verbose -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número de dispositivo</span>

- Muestra sólo los dispositivos con un ID de proveedor y producto determinados:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vendedor</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">producto</span>
