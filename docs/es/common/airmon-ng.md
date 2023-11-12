---
layout: page
title: common/airmon-ng (español)
description: "Activa el modo monitor en dispositivos de red inalámbricos."
content_hash: 55ba6fd7decad0a81ae6e44015d7dd1fc24091ac
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
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
tldri18n_status: 2
---
# airmon-ng

Activa el modo monitor en dispositivos de red inalámbricos.
Parte de `aircrack-ng`.
Más información: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Lista dispositivos inalámbricos y sus estados:

`sudo airmon-ng`

- Activa el modo monitor para un dispositivo específico:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Elimina los procesos perturbadores que utilizan dispositivos inalámbricos:

`sudo airmon-ng check kill`

- Desactiva el modo monitor para una interfaz de red específica:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
