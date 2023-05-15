---
layout: page
title: common/aircrack-ng (español)
description: "Crackea claves WEP y WPA/WPA2 desde handshake en paquetes capturados."
content_hash: a2326e3477dc683a22d5aa6c884795aa193eca10
last_modified_at: 2023-05-15
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aircrack-ng

Crackea claves WEP y WPA/WPA2 desde handshake en paquetes capturados.
Parte de la suite de software de red Aircrack-ng.
Más información: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Crackea la clave desde el archivo de captura usando [w]ordlist:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/lista.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/captura.cap</span>

- Descifra la clave del archivo de captura utilizando [w]ordlist y el [e]ssid del punto de acceso:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/lista.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/captura.cap</span>

- Descifra la clave del archivo de captura utilizando [w]ordlist y la dirección MAC del punto de acceso:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/lista.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/captura.cap</span>
