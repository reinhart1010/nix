---
layout: page
title: linux/lsusb (español)
description: "Muestra información sobre puertos y dispositivos USB."
content_hash: 64653c7d1944599a49e2cffcc54c27af3335575c
related_topics:
  - title: English version
    url: /en/linux/lsusb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/lsusb.html
    icon: bi bi-globe
---
# lsusb

Muestra información sobre puertos y dispositivos USB.
Más información: <https://manned.org/lsusb>.

- Lista todos los dispositivos USB disponibles:

`lsusb`

- Lista la jerarquía de dispositivos USB en forma de árbol:

`lsusb -t`

- Lista los dispositivos USB de forma verbosa:

`lsusb --verbose`

- Lista información detallada acerca de un dispositivo USB determinado:

`lsusb -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>

- Lista solo dispositivos con un ID de ensamblador y producto determinado:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ensamblador</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">producto</span>
