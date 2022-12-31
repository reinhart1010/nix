---
layout: page
title: common/airmon-ng (español)
description: "Activar el modo monitor en dispositivos de red inalámbricos."
content_hash: 18c6a08e6d04ca65c46bc8e8e4cf14c8a8c31513
last_modified_at: 2022-12-31
related_topics:
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airmon-ng

Activar el modo monitor en dispositivos de red inalámbricos.
Parte ode `aircrack-ng`.
Más información: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista de dispositivos inalámbricos y sus estados:

`sudo airmon-ng`

- Activar el modo monitor para un dispositivo específico:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Elimina los procesos perturbadores que utilizan dispositivos inalámbricos:

`sudo airmon-ng check kill`

- Desactiva el modo monitor para una interfaz de red específica:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
